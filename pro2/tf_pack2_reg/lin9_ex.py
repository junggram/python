# https://github.com/pykwon/python/tree/master/data
#
# 자전거 공유 시스템 분석용 데이터 train.csv를 이용하여 대여횟수에 영향을 주는 변수들을 골라 다중선형회귀분석 모델을 작성하시오.
# 모델 학습시에 발생하는 loss를 시각화하고 설명력을 출력하시오.
# 새로운 데이터를 input 함수를 사용해 키보드로 입력하여 대여횟수 예측결과를 콘솔로 출력하시오.

import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost import plot_importance
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score


data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/data/train.csv' )
data = data.iloc[:,1:12]
print(data.head(3),data.shape)
print(data.info())

features = data.iloc[:,0:10]
labels = data.iloc[:,10]
print(np.array(features))
print(np.array(labels))

#상관계수 확인
co_re=data.corr()
print(co_re['count'].sort_values(ascending=False))

# for i  in range(10): # 개개인별 상관관계
#     print(features.iloc[:,i])
#     print(np.corrcoef(features.iloc[:,i], labels)) 
    # temp(0.3944), atemp(0.3897), humidity(-0.3173), casual(0.6904), registered(0.9709) 를 쓸게용

features = features.loc[:,['temp', 
                           # 'atemp',
                           'humidity',
                           'casual',
                           'registered']]
# temp, atemp 는 상관관계가 높을 것으로 염려가 됨 (독립성, 다중공선성 불만족)
# 그렇기 때문에 하나를뺴자
# print(features.head(3))

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
features = scaler.fit_transform(features) # nan나서 스케일링 해줌

# model = xgb.XGBClassifier(n_estimators = 500, random_state=12).fit(features, labels)
#
# fig, ax = plt.subplots(figsize = (10, 12))
# plot_importance(model, ax = ax)
# plt.show()

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.3, random_state=12)

print('-------------------------------------')
model2 = Sequential()
model2.add(Dense(units=1, input_dim=4, activation='linear'))
model2.compile(optimizer='sgd', loss='mse', metrics=['mse']) # 과적합 의심이 된다면 다른 방법을 써보자 (RMSprop, Adam 등)
history = model2.fit(x_train, y_train, epochs=17, verbose=2, validation_split=0.15) # 학습 / ValueError: Input contains NaN, infinity or a value too large for dtype('float32').
print('train / test 후 평가 :', model2.evaluate(x_test, y_test, verbose=0))

import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label = 'train loss')
plt.xlabel('epochs')
plt.show()

print()
pred2 = model2.predict(x_test)
print('train / test 후 결정계수 :',r2_score(y_test,pred2)) 