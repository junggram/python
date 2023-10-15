# pima=indians-diabetes dataset 으로 당뇨병 유무 분류 모델

import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics._scorer import accuracy_scorer

# Pregnancies: 임신 횟수
# Glucose: 포도당 부하 검사 수치
# BloodPressure: 혈압(mm Hg)
# SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
# Insulin: 혈청 인슐린(mu U/ml)
# BMI: 체질량지수(체중(kg)/(키(m))^2)
# DiabetesPedigreeFunction: 당뇨 내력 가중치 값
# Age: 나이
# Outcome: 클래스 결정 값(0또는 1)

url = '../testdata/prima-indians-diabetes.csv'
df = pd.read_csv(url, names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome'])
print(df.head(3),df.shape) # (768, 9)

array = df.values
print(array)
x = array[:,0:8] # 슬라이싱
y = array[:,8] # 인덱싱
print(x.shape, y.shape) # (768, 8) (768,)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size=0.3, random_state=7)
print(x_train.shape, x_test.shape) # (537, 8) (231, 8)

model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 :', model.predict(x_test[:10]))
print('실제값 :', y_test[:10])
print((model.predict(x_test) !=y_test).sum()) # 58
print('test로 검정한 분류 정확도 :', model.score(x_test, y_test)) # 0.7489
print('train로 검정한 분류 정확도 :', model.score(x_train, y_train)) # 0.7839    # test의 분류정확도와, train의 분류정확도가 크면 좋지 않다.

from sklearn.metrics import accuracy_score
pred = model.predict(x_test)
print('분류 정확도 :',accuracy_score(y_test,pred)) # 분류 정확도 : 0.7489

import joblib
import pickle

# 학습이 끝난 모델은 저장

joblib.dump(model, 'pima_model.csv')
# pickle.dump(model, open('pima_model.dat','wb'))

mymodel = joblib.load('pima_model.csv')
# mymodel = pickle.load(open('pima_model.dat','rb'))
print('test로 검정한 분류 정확도 :', mymodel.score(x_test, y_test))

# 새로운 값으로 예측
print(x_test[:1])
print(mymodel.predict([[ 1.,   90.,   62.,   12.,   43.,   27.2,   0.58, 24.  ]]))