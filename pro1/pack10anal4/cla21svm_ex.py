# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
# https://www.kaggle.com/zhaoyingzhu/heartcsv
# https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv
#
# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ

# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)

# 데이터 예)
# "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
# "1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
# "2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"
# ...

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score



data = pd.read_csv('../testdata/Heart.csv')
print(data.head(3))
mean = data['Ca'].mean() # 평균
# print(mean)
data = data.fillna(mean) # null값 평균 대체

x = data.iloc[:,1:14]
y = data.iloc[:,14]

print(x.info()) # 문자데이터 칼럼확인
x = x.drop(columns=['ChestPain','Thal'])
# print(x)
y = y.map({'Yes' : 0, 'No' : 1}) # dummy 
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (212, 13) (91, 13) (212,) (91,)

model = svm.SVC(C=0.1).fit(x_train, y_train)
pred = model.predict(x_test) 
print('예상치 :', pred[:10]) # 예상치 : [1 1 1 1 1 1 1 1 1 1]
print('실제값 :', y_test.values[:10]) # 실제값 : [1 1 1 1 0 1 0 0 1 0]
print('분류정확도 :', accuracy_score(y_test,pred)) # 분류정확도 : 0.560

# 새로운 값으로 예상
new_data = [[63,1,145,233,1,2,150,0,2.3,3,0]]

pred = model.predict(new_data)
print(pred)

    
    





