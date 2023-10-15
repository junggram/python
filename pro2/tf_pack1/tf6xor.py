# 논리게이트 중 XOR는 복수의 뉴런(노드)를 사용해야한다

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adam

# 논리회로 분류 모델 생성
x = np.array([[0,0],[0,1],[1,0],[1,1]])
print(x)
y = np.array([0,1,1,0]) # xor

model = Sequential()
'''
model.add(Dense(units=5, input_dim=2))      # 첫번째 레이어
model.add(Activation('relu'))               # 중간에서는 활성함수를 ReLu를 사용
# model.add(Dense(units=5))                   # 두번째 레이어
# model.add(Activation('relu'))               # 중간에서는 활성함수를 ReLu를 사용
model.add(Dense(1))                         # 세번째 레이어 - 이처럼 레이어를 쌓아가는게 keras의 핵심, 설계도를 작성
model.add(Activation('sigmoid'))            
'''
# model.add(Flatten(input_dim=2)) # 차원을 줄여서 결과를 출력하는 flatten()과 다른것임
# model.add(Dense(units=5, activation='relu'))

# model.add(Dense(units=5, input_shape=(2,), activation='relu')) # input_dim = input_shape : 튜플타입으로 써야함
model.add(Dense(units=5, input_dim=2, activation='relu')) # 위 두줄을 한줄로 쓴 모양
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1, activation='sigmoid')) # 위 설계도를 줄여서 쓴 모양
print(model.summary()) # 설계된 모델의 layer, parameter 확인

model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])



# 모델 학습
# model.fit(x, y, epochs=100, batch_size=1, verbose=1)
history = model.fit(x, y, epochs=100, batch_size=1, verbose=1)
print('\nhistory :', history.history['loss'])
print('accuracy :', history.history['accuracy'])






# 모델 평가
loss_metrics = model.evaluate(x = x, y = y, 
                               batch_size = 1,
                                verbose = 0)
print('loss :', loss_metrics[0], 'accuracy :',loss_metrics[1])




# 모델 사용
pred = (model.predict(x) > 0.5).astype('int32') # 0.5를 기준으로  1 or 0 으로 분류
print('pred :', pred.flatten()) # flatten() : 차원 축소

print()
print(model.input)
print(model.output)
print(model.weights) # karnel : 가중치, bias 값 확인

# history 값 시각화
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label = 'train loss')
plt.plot(history.history['accuracy'], label = 'train acc')
plt.xlabel('epochs')
plt.show()