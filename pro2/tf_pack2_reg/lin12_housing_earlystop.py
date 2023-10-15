# 활성화 함수, 학습 조기 종료

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import boston_housing

print(boston_housing.load_data())
(x_train, y_train), (x_test, y_test) = boston_housing.load_data() # (404, 13) (404,) (102, 13) (102,)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
print(x_train[0])
print(y_train[0])

# 데이터 정규화 : (관찰값 - 평균) / 표준편차
x_mean = x_train.mean(axis=0)
x_std = x_train.std(axis=0)

x_train -= x_mean
x_train /= x_std

x_test -= x_mean
x_test /= x_std
#-----------------------------------
y_mean = y_train.mean(axis=0)
y_std = y_train.std(axis=0)

y_train -= y_mean
y_train /= y_std

y_test -= y_mean
y_test /= y_std
#-----------------------------------
print(x_train[0])
print(y_train[0])

# model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=35, activation='relu'),
    tf.keras.layers.Dense(units=24, activation='relu'),
    tf.keras.layers.Dense(units=1)  
    ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), loss='mse', metrics=['mse'])
model.summary()

# 활성화 함수 비교
import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

x = np.arange(-5, 5, 0.01)
sigmoid_x = [sigmoid(z) for z in x]
tanh_x = [math.tanh(z) for z in x]
relu = [0 if z < 0 else z for z in x]
plt.axhline(0, color='gray')
plt.axvline(0, color='red')
plt.plot(x, sigmoid_x,'b-', label='sigmoid')
plt.plot(x, tanh_x,'r--', label='tanh')
plt.plot(x, relu,'g.', label='relu')
plt.show()

history = model.fit(x_train, y_train, epochs = 25, batch_size = 32, validation_split = 0.25)

plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

print(model.evaluate(x_test, y_test))

# 주택가격(실제, 예측) 시각화
pred_y = model.predict(x_test) 
plt.figure(figsize=(5,5))
plt.plot(y_test, pred_y, 'b.')
plt.xlabel('y_test')
plt.ylabel('pred_y')
plt.show()

# 학습 조기 종료
model2 = tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=35, activation='relu'),
    tf.keras.layers.Dense(units=24, activation='relu'),
    tf.keras.layers.Dense(units=1)  
    ])

model2.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), loss='mse', metrics=['mse'])

history2 = model2.fit(x_train, y_train, epochs = 1000, batch_size = 1,
                       validation_split = 0.25,
                       callbacks = [tf.keras.callbacks.EarlyStopping(   # 조기종료
                           monitor='val_loss',  # 타겟 : loss 말고 val_loss로 타겟을 잡아라                
                           patience=3,          # 얼마까지 
                           )] 
                       )
plt.plot(history2.history['loss'], 'b-', label='loss')
plt.plot(history2.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

print(model.evaluate(x_test, y_test))