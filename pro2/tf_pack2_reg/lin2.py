# 선형회귀 모형 작성 : 수식 사용
# tensorflow 사용

import tensorflow as tf
import numpy as np
from keras.optimizers import SGD, RMSprop, Adam




tf.random.set_seed(123)
w = tf.Variable(tf.random.normal((1,)))
b = tf.Variable(tf.random.normal((1,)))
print(w.numpy(), ' ', b.numpy())

x = [1., 2., 3., 4., 5.]
y = [1.2, 2.8, 3.0, 3.5, 6.0] 
print(np.corrcoef(x,y))     # r = 0.937     # 인과 관계가 있다 가정하고 회귀분석 작업을 진행








# 선형회귀식을 얻기 위해 cost를 줄여가는 작업
opti = SGD() # optimizer

@tf.function
def train_func(x,y):
    with tf.GradientTape() as tape: # 
        hypo = tf.add(tf.multiply(w,x),b) # y = wx + b
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo,y))) # cost (loss) = ((예측값 - 실제값)**2 )의 합의 평균
    
    grad = tape.gradient(loss, [w, b]) # 자동 미분을 해줌
    opti.apply_gradients(zip(grad, [w, b])) # 경사하강법
    return loss
    

w_vals=[]
cost_vals=[]

for i in range(1, 101): # epochs
    loss_val = train_func(x,y)
    cost_vals.append(loss_val.numpy())
    w_vals.append(w.numpy())
    if i % 10 == 0:
        print(loss_val) # loss값 출력
        
print('cost :', cost_vals) # cost : [5.1111007, 3.101682, 1.9306889, ...]
print('w :', w_vals) # w : [array([0.58158505], dtype=float32), array([0.6925764], dtype=float32), ...]








# w, cost,를 시각화
import matplotlib.pyplot as plt
plt.plot(w_vals, cost_vals, 'o--')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()

print('cost가 최소일 때 w :',w.numpy()) # w : [0.90847826]
print('cost가 최소일 때 b :',b.numpy()) # b : [0.6487321]    # yhat = 0.90847826 * x + 0.6487321







# 선형회귀식으로 시각화
y_pred = tf.multiply(x,w) + b
print('y_pred :', y_pred)
print('y :', y)

plt.plot(x, y,'+', label = 'real' )
plt.plot(x, y_pred,'b-', label = 'pred' ) # 회귀선
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()





print()
# 새 값으로 정량적 예측
new_x = [3.5, 9.7]
new_pred = tf.multiply(new_x,w) + b
print('new_pred :', new_pred.numpy())