# tf.constant() : 텐서(일반적으로 상수)를 직접 기억
# tf.Variable() : 텐서가 저장된 주소를 참조

import tensorflow as tf
import numpy  as np

node1 = tf.constant(3, tf.float32)
node2 = tf.constant(4.0)
print(node1)
print(node2)
imsi = tf.add(node1,node2)
print(imsi)

print()
node3 = tf.Variable(3, dtype = tf.float32)
node4 = tf.Variable(4.0)
print(node3)
print(node4)
node4.assign_add(node3)
print(node4)

print()
a = tf.constant(5)
b = tf.constant(10)
c = tf.multiply(a,b)
print(c)
result = tf.cond(a < b, lambda:tf.add(10,c), lambda:tf.square(a))
print('result :',result)

print('---------- 함수 관련 : autograph (Graph 객체 환경에서 작업하도록 함)------------')
v = tf.Variable(1)

def find_next_func():
    v.assign(v+1)
    if tf.equal(v % 2, 0):
        v.assign(v+10)
        
find_next_func()
print(v.numpy())
print(type(find_next_func)) # <class 'function'>

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
def func1(): # 1부터 3까지 증가
    imsi = tf.constant(0)
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
        # imsi = imsi +su
        # imsi += su
        
    return imsi

kbs = func1()
print(kbs.numpy(), ' ', np.array(kbs))

print('^^^^^^^^^^^^^^^^^^^ func2 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
imsi = tf.constant(0)

@tf.function
def func2(): # 1부터 3까지 증가
    # imsi = tf.constant(0)
    global imsi # 아래 local variable 에러때문에 글로벌 imsi 참조
    su = 1
    for _ in range(3):
        
        imsi = tf.add(imsi, su)
        # imsi = imsi +su
        # imsi += su
        
    return imsi
mbc = func2()
print(mbc.numpy(), ' ', np.array(mbc))
    
print('^^^^^^^^^^^^^^^^^^^ func3 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
imsi = tf.Variable(0)           # @tf.function 있을땐 여기

@tf.function
def func3():
    # imsi = tf.Variable(0)     # @tf.function 없을땐 여기  /  auto graph에서는 tf.Variable()은 함수 밖에 선언
    su = 1
    for _ in range(3):
        
        # imsi = tf.add(imsi, su)
        # imsi = imsi +su
        # imsi += su
        imsi.assign_add(su)
        
    return imsi
    
sbs = func3()
print(sbs.numpy(), ' ',np.array(sbs))

print('구구단 출력 (졸려용)-------------------------------------------')
@tf.function
def gugu1(dan):
    su = 0   # su = tf.constant(0)
    for _ in range(9):
        su = tf.add(su, 1) 
        # print(su.numpy()) # auto graph에서는 tensor연산에만 집중 , numpy지원 안함     # 'Tensor' object has no attribute 'numpy'
        print('{} x {} = {}'.format(dan, su, dan*su)) # auto graph에서는 tensor연산에만 집중, format 지원안함
        # TypeError: unsupported format string passed to Tensor.__format__
        
        
gugu1(3)

print()
@tf.function
def gugu2(dan):
    for i in range(1,10):
        result = tf.multiply(dan, i)  # 원소 곱하기, tf.matmul() : 행렬곱
        print('{} x {} = {}'.format(dan, i, result))
        
gugu2(2)

