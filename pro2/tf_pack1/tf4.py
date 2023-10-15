# 연산자와 기본 함수 경험

import tensorflow as tf
import numpy as np

x = tf.constant(7)
y = tf.constant(3)

print(x + y)
print(tf.add(x,y))

print(tf.cond(x > y, lambda:tf.add(x,y), lambda:tf.subtract(x, y)))

f1 = lambda: tf.constant(123)
f2 = lambda: tf.constant(456)

imsi = tf.case([(tf.greater(x,y), f1)], default = f2)  # tf.less 도있음  if(x > y) return 123 else return 456
print(imsi.numpy()) 

print('\n관계연산')
print(tf.equal(1,2).numpy())
print(tf.not_equal(1,2).numpy())
print(tf.greater(1,2).numpy())
print(tf.greater_equal(1,2).numpy())
print(tf.less(1,2).numpy())

print('\n논리연산')
print(tf.logical_and(True, False).numpy())
print(tf.logical_or(True, False).numpy())
print(tf.logical_not(True).numpy())

kbs = tf.constant([1,2,2,2,3])
val, idx = tf.unique(kbs)
print(val.numpy())
print(idx.numpy())

print()
# tf.reduce~ : 차원 축소
ar = [[1,2],[3,4]]
print(tf.reduce_mean(ar).numpy()) # 전체 평균
print(tf.reduce_mean(ar, axis=0).numpy()) # 열 평균
print(tf.reduce_mean(ar, axis=1).numpy()) # 행 평균

t = np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]]) # (2, 2, 3) : 2면, 2행 3열
print(t.shape)
print(tf.reshape(t, shape=[2,6])) # 차원 변경                                     # 2행 6열
print(tf.reshape(t, shape=[-1,6])) # 갯수를 모르겠을 때 -1로 채워놓으면 알아서 맞게 해줌   # ?행 6열
print(tf.reshape(t, shape=[2,-1])) # 갯수를 모르겠을 때 -1로 채워놓으면 알아서 맞게 해줌   # 2행 ?열
print()

# 차원 축소
aa = np.array([[1],[2],[3],[4]])
print(aa.shape) # (4, 1)
bb = tf.squeeze(aa)
print(bb.shape) # (4,) 차원축소됨
print()
aa2 = np.array([[[1],[2]],[[3],[4]]])
print(aa2.shape) # (2, 2, 1)
print(aa2)
'''
[[[1]
  [2]]

 [[3]
  [4]]]
'''
bb2 = tf.squeeze(aa2)
print(bb2.shape) # (2, 2)
print(bb2)
'''
[[1 2]
 [3 4]]
'''

print()
print(t.shape)
t2 = tf.squeeze(t)
print(t2.shape)
print(t2)

print()
# 차원 확대
'''
tarr = tf.constant([[1,2,3],[4,5,6]])
print(tarr, tarr.shape) # (2, 3)

sbs = tf.expand_dims(tarr, 0) # 첫번째 차원을 추가해 확장
print(sbs, sbs.shape) # (1, 2, 3)

sbs2 = tf.expand_dims(tarr, 1) # 두번째 차원을 추가해 확장
print(sbs2, sbs2.shape) # (2, 1, 3)

sbs3 = tf.expand_dims(tarr, 2) # 세번째 차원을 추가해 확장
print(sbs3, sbs3.shape) # (2, 3, 1)

sbs4 = tf.expand_dims(tarr, -1) # -1을 입력하면 제일 마지막 차원을 추가해 확장
print(sbs4, sbs4.shape) # (2, 3, 1)
'''

tarr = tf.constant([[1,2,3],[4,5,6]])
print(tarr, tf.shape(tarr).numpy())  # 2행 3열 [2 3]
sbs = tf.expand_dims(tarr, 0)  # 첫번째 차원을 추가해 확장 
print(sbs, tf.shape(sbs).numpy())  # 2차원에서 3차원으로
print()
sbs2 = tf.expand_dims(tarr, 1)  # 두번째 차원을 추가해 확장 
print(sbs2, tf.shape(sbs2).numpy())
print()
sbs3 = tf.expand_dims(tarr, 2)  # 세번째 차원을 추가해 확장 
print(sbs3, tf.shape(sbs3).numpy()) # 2면 3행 1열

print('one-hot')
print(tf.one_hot([0,1,2,3], depth = 4))
print(tf.argmax(tf.one_hot([0,1,2,3], depth = 4)).numpy()) # 