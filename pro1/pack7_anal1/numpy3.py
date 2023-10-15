# 배열 연산

import numpy as np
x = np.array([[1,2],[3,4]]) # 모든 타입이 int
print(x,x.dtype)
x = np.array([[1,2],['3',4]]) # 모든 타입이 string
print(x,x.dtype)
x = np.array([[1,2],[3.0,4]]) # 모든 타입이 float
print(x,x.dtype)
x = np.array([[1,2],[3,4]], dtype=np.float64) # dtype을 직접 입력하면 바꿔줌
print(x,x.dtype)


y = np.arange(5,9).reshape(2,2)
print(y, y.dtype)
y = y.astype(np.float32)
print(y, y.dtype)

print()
print(x + y) # 요소끼리의 연산
print(np.add(x,y)) # 요소끼리의 연산
# imsi=np.random.rand(10000000)
# print(imsi)
# print(sum(imsi)) # 파이썬 연산함수
# print(np.sum(imsi)) # numpy 연산함수 : 파이썬 연산 함수보다 속도가 빠름

print()
print(x - y)
print(np.subtract(x,y))

print()
print(x * y)
print(np.multiply(x,y))

print()
print(x * y)
print(np.divide(x,y))

print()
# 벡터 간 내적 연산 : dot 참고 a %*% b  ( 행렬곱 )
v = np.array([9,10])
w = np.array([11,12])
print(v * w)
print(v.dot(w)) # 파이썬 연산 , v[0]*w[0] + v[1]*w[1]
print(np.dot(v,w)) # numpy 연산 , 위와 같음

print()
print(x) # 2행 2열
print(v) # 1행 2열
print(np.dot(x,v)) # x[0,0]*v[0] + x[0,1]*v[1] = 29, x[1,0]*v[0] + x[1,1]*v[1] = 67

print() 
print(x) # 2행 2열
print(y) # 2행 2열
print(np.dot(x,v)) # x[0,0]*y[0,0] + x[0,1]*y[1,0] = 19, ...

print('---------------------')
print(np.sum(x))
print(np.mean(x))
print(np.cumsum(x)) # 누적 합 (요소들의 합)
print(np.cumprod(x)) # 누적 곱 (요소들의 곱)
#...

print()
name1 = np.array(['tom','james','tom','oscar'])
name2 = np.array(['tom','page','john'])
print(np.unique(name1)) # 중복 배제
print(np.intersect1d(name1,name2, assume_unique=True)) # 교집합, 중복 허용
print(np.union1d(name1,name2)) # 합집합

print('\nTranspose : 전치', '행과 열을 바꿈')
print(x)
print(x.T)
print(x.transpose())
print(x.swapaxes(0,1))

print('\nBroadcast 연산 : 크기가 다른 배열 간의 연산을 하면 작은 배열이 큰 배열의 크기를 자동으로 따라감')
x = np.arange(1,10).reshape(3,3)
print(x,'연산전')
y = np.array([1,0,1])
print(y,'연산전')
print(x + y,'연산후')

print()
print(x,'불러오기전')
np.savetxt('my.txt',x)
imsi = np.loadtxt('my.txt')
print(imsi,'불러온것')

print()

imsi2=np.loadtxt('my2.txt',delimiter=',') # 배열을 만들어서 불러오기
print(imsi2)


