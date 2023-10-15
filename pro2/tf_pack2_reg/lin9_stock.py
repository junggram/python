# 주식 데이터로 예측 모형 작성. 전날 데이터로 다음날 종가 예측

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

xy = np.loadtxt('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/stockdaily.csv',
                 delimiter = ',', skiprows=1)

print(xy[:2], xy.shape)

x_data = xy[:,0:-1] # 2차원
scaler = MinMaxScaler(feature_range=(0,1)) # 칼럼간 단위 차이가 많이 나서 평가과정에서 nan이 나와서 정규화를 해줬음
x_data = scaler.fit_transform(x_data)
print(x_data[:2])
y_data = xy[:,[-1]] # 2차원
print(y_data[:2])

# 이전일 시가(Open), 고가(High), 저가(Low), 거래량(Volume)와 다음날 종가(Close)를 한 행으로 만들기
print(x_data[0], y_data[0])
print(x_data[1], y_data[1])
print()

x_data = np.delete(x_data, -1, axis=0)
y_data = np.delete(y_data,0)
print(x_data[0], y_data[0])
print()

print('-------------------------------------')
# (train, test 는 생략했음)
model = Sequential()
model.add(Dense(units=1, input_dim=4, activation='linear'))

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(x_data, y_data, epochs=200, verbose=0, validation_split=0.2) # 학습
print('train / test 없이 평가 :', model.evaluate(x_data, y_data, verbose=0))

print(x_data[10]) # 임의의 자료로 예측값과 실제값 비교 (모든 자료로 해도 됨~~~)
test = x_data[10].reshape(-1,4)
print('실제값 :', y_data[10])
print('예측값 :', model.predict(test,verbose=0))

print()
pred = model.predict(x_data)
from sklearn.metrics import r2_score
print('train / test 없이 결정계수 :',r2_score(y_data,pred)) # 0.9938 과적합(overfitting)이 의심됨

# train / test 전 모델로 시각화
plt.plot(y_data, 'b')
plt.plot(pred,'r--')
plt.show()

print('\n 과적합 방지를 목적으로 학습/검정 데이터로 분리 ---')
# print(len(x_data))
# train_size = int(len(x_data) *0.7)
# test_size = len(x_data) - train_size
# print(train_size, ' ', test_size)
# x_train, x_test = x_data[0:train_size], x_data[train_size:len(x_data)]
# y_train, y_test = y_data[0:train_size], y_data[train_size:len(x_data)]
# print(x_train[:2], x_train.shape)
# print(x_test[:2], x_test.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=0.3, shuffle = False)
print(x_train[:2], x_train.shape)
print(x_test[:2], x_test.shape)

print('-------------------------------------')
model2 = Sequential()
model2.add(Dense(units=1, input_dim=4, activation='linear'))

model2.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model2.fit(x_train, y_train, epochs=200, verbose=0) # 학습
print('train / test 없이 평가 :', model2.evaluate(x_test, y_test, verbose=0))

print(x_test[10]) # 임의의 자료로 예측값과 실제값 비교 (모든 자료로 해도 됨~~~)
test2 = x_test[10].reshape(-1,4)
print('실제값 :', y_test[10])
print('예측값 :', model2.predict(test2,verbose=0))

print()
pred2 = model2.predict(x_test)
print('train / test 후 결정계수 :',r2_score(y_test,pred2)) # 0.947

# train / test 후 모델로 시각화
plt.plot(y_test, 'b')
plt.plot(pred2,'r--')
plt.show()

print('-------------------------------------')
# (train, test 는 생략했음)
model3 = Sequential()
model3.add(Dense(units=1, input_dim=4, activation='linear'))

model3.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model3.fit(x_train, y_train, epochs=200, verbose=0, validation_split=0.15) # 학습
print('train / test validation 후 평가 :', model2.evaluate(x_test, y_test, verbose=0))

print()
pred3 = model3.predict(x_test)
print('train / test 후 결정계수 :',r2_score(y_test,pred3)) # 0.947

# train / test 후 모델로 시각화
plt.plot(y_test, 'b')
plt.plot(pred3,'r--')
plt.show()

# 머신러닝의 이슈 : 모델의 최적화(optimizaion)와 일반화(포용성, generalization) 사이의 줄다리기이다