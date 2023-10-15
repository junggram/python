import tensorflow as tf
import os
# SSE 및 AVX 등의 경고는 소스를 빌드 하면 없어지지만, 명시적으로 경고 없애기
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print("즉시 실행 모드: ", tf.executing_eagerly())
print("GPU ", "사용 가능" if tf.test.is_gpu_available() else "사용 불가능")
print(tf.__version__) # 2.11.0




# 텐서(tensor)는 배열(array)이나 행렬(matrix)과 매우 유사한 특수한 자료구조입니다.
# 텐서는 GPU나 다른 연산 가속을 위한 특수한 하드웨어에서 실행할 수 있다는 점을 제외하면, 텐서는 NumPy의 ndarray와 매우 유사
# tensorflow 는 numpy 기반

print()
# 상수 선언
print(1, type(1))
print(tf.constant(1), type(tf.constant(1))) # 1, shape=() / scalar : 0-d tensor = 0차원 스칼라
print(tf.constant([1])) # [1], shape=(1,) / vector : 1-d tensor = 1차원 배열
print(tf.constant([[1]])) # [[1]], shape=(1, 1) / matrix : 2-d tensor = 2차원 배열

print(tf.rank(tf.constant(1)), ' ', tf.rank(tf.constant([1])), ' ', tf.rank(tf.constant([[1]])))
# tf.Tensor(0, shape=(), dtype=int32)   tf.Tensor(1, shape=(), dtype=int32)   tf.Tensor(2, shape=(), dtype=int32)

print()
a = tf.constant([1,2])
b = tf.constant([3,4])
c = a + b
print(c) # tf.Tensor([4 6], shape=(2,), dtype=int32)
# 2.xx 버전에서는 내부적으로(세션에서) 연산이 되고있는 그래프가 있는데 보이지않는다. (1.xx버전에서는 다 보여줘서 배우기가 힘들었다)
c = tf.add(a, b)
print(c)

print()
# d = tf.constant([3])
d = tf.constant([[3]])
e = c + d
print(e) # tf.Tensor([7 9], shape=(2,), dtype=int32) / Broadcasting

print(1 + 2)
print(tf.constant([1]) + tf.constant([2]))

print()
print(7)
print(tf.convert_to_tensor(7, dtype = tf.float32)) # dtype을 바꿀 수도 있음~
print(tf.cast(7, dtype = tf.float32)) # dtype을 바꿀 수도 있음~
print(tf.constant(7.0))
print(tf.constant(7, dtype=tf.float32)) # dtype을 바꿀 수도 있음~

print()
# numpy의 ndarray와 tensor 사이에 type 변환
import numpy as np
arr = np.array([1,2])
print(arr, type(arr)) # [1 2] <class 'numpy.ndarray'>
print(arr + 5) # [6 7] <class 'numpy.ndarray'>

tfarr = tf.add(arr, 5)
print(tfarr, type(tfarr)) # tf.Tensor([6 7], shape=(2,), dtype=int32) <class 'tensorflow.python.framework.ops.EagerTensor'>
# ndarray가 자동으로 tensor로 변환

print(tfarr.numpy()) # numpy로 강제 형변환
print(np.add(tfarr,3)) # numpy로 자동 형변환
print(list(tfarr.numpy()))

