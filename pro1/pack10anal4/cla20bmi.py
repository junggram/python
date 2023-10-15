# 체질량지수(BMI)는 자신의 몸무게(kg)를 키의 제곱을 100으로 나눈 값

print( 65 / ((168/100) * (168/100)))
'''
import random
random.seed(12)

def calc_bmi(h,w):
    bmi = w / (h / 100)**2
    if bmi < 18.5: return 'thin'
    if bmi < 25.0: return 'normal'
    return 'fat'
    
# print(calc_bmi(168,65))  

fp = open('bmi.csv','w')
fp.write('height,weight,label\n')


# 무작위로 데이터 생성

cnt = {'thin' :0, 'normal':0, 'fat': 0}

for i in range(50000):
    h = random.randint(150,200)
    w = random.randint(35,100)
    label = calc_bmi(h,w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h,w,label))
    
fp.close()
'''
import pandas as pd
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

tbl = pd.read_csv('bmi.csv')
print(tbl.head(3),tbl.shape)
print(tbl.describe())

label = tbl['label']
print(label[:3])

w = tbl['weight'] / 100 # 정규화
h = tbl['height'] / 200 # 정규화
print(w[:3])
print(h[:3])

wh = pd.concat([w,h],axis=1)
print(wh[:3], wh.shape)

# label 을 dummy
label = label.map({'thin':0,'normal':1,'fat':2})
print(label[:3])

# train / test split
x_train, x_test, y_train, y_test = train_test_split(wh,label,test_size=0.3,random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (35000, 2) (15000, 2) (35000,) (15000,)

print()

# model
model = svm.SVC(C=0.1).fit(x_train, y_train)

pred = model.predict(x_test)
print('예측값 :', pred[:10])
print('실제값 :', y_test[:10].values)

acc = metrics.accuracy_score(y_test, pred)
print('acc :', acc)

print()
# 교차 검증
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, wh, label, cv = 3)
print('각각의 검증 정확도 :', cross_vali) # 각각의 검증 정확도 : [0.99232015 0.99346013 0.99057962]
print('평균 검증 정확도 :', cross_vali.mean()) # 평균 검증 정확도 : 0.9921199691930799

# 시각화
tbl2 = pd.read_csv('bmi.csv', index_col=2)

def scatter_func(label, color):
    b = tbl2.loc[label]
    plt.scatter(b['weight'], b['height'], c= color, label = label)
    
scatter_func('fat', 'red')
scatter_func('normal', 'white')
scatter_func('thin', 'blue')

plt.legend()
plt.show()

# 새 값으로 예측
new_data = pd.DataFrame({'weight':[66,55], 'height':[170,180]})
new_data['weight'] = new_data['weight'] / 100
new_data['height'] = new_data['height'] / 200
new_pred = model.predict(new_data)
print('새로운 예측값 :',new_pred)