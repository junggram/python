# 배열에 행/열 추가

import numpy as np

aa = np.eye(3)
print(aa)
print(aa.shape)
print(type(aa))
print(type(aa[2]))
print(type([aa[2]]))
# 열 추가
bb = np.c_[aa,aa[2]] # aa의 3열과 동일한 열을 추가  # <class 'numpy.ndarray'>
print(bb)

# 행 추가
cc = np.r_[aa,[aa[2]]] # aa의 3행과 동일한 행을 추가 # <class 'list'>
print(cc)

print()
a = np.array([1,2,3])
print('a = ',a) # 1차원으로 나옴
print(np.c_[a]) # 2차원으로 확대되고 열추가가 됨
print(a.reshape(3,1)) # 2차원으로 확대되고 열추가가 됨

print('---append, insert, delete---')
print(a)
# b = np.append(a,[4,5])
b = np.append(a,[4,5], axis=0) # axis = 0(열 방향으로,행 기준으로) or 1(행 방향으로,열 기준으로) 
print(b)

c= np.insert(a,0,[6,7],axis=0) # a,위치,요소,방향, 0번째에 6,7 요소를 열 방향으로 추가
print(c)

# d = np.delete(a,1)
# d = np.delete(a,[1])
d = np.delete(a,[1,2])
print(d)

print('--------------2차원------------------')

aa = np.arange(1,10).reshape(3,3)
print(aa)
print(np.insert(aa,1,99)) # 2차원이었는데 1차원으로 바뀌고 2번째 지점에 99를 추가함
print(np.insert(aa,1,99, axis=0)) # * 차원유지 *, axis = 0(열 방향으로,행 기준으로) = 2번째 행에 99를 추가
print(np.insert(aa,1,99, axis=1)) # * 차원유지 *, axis = 1(행 방향으로,열 기준으로) = 2번째 열에 99를 추가

print()
print(aa)
bb = np.arange(10,19).reshape(3,3)
print(bb)

cc = np.append(aa,bb)
print(cc)

cc = np.append(aa,bb, axis = 0) # shape이 같아야함
print(cc)

cc = np.append(aa,bb, axis = 1) # shape이 같아야함
print(cc)

print(np.delete(aa,1))
print(np.delete(aa,1,axis=0))
print(np.delete(aa,1,axis=1))