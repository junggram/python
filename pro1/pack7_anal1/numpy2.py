# numpy
import numpy as np

ss=['tom','james','oscar',1] # <class 'list'>
print(ss, type(ss)) # ['tom', 'james', 'oscar', 1]  =  data type이 다를 수 있다 (string, int가 들어있음)

ss2=np.array(ss) # <class 'numpy.ndarray'>
print(ss2, type(ss2))  # ['tom' 'james' 'oscar' '1'] = data type이 다를 수 없다 (int가 string type으로 변환돼서 들어있음)

# 메모리 비교 (list vs numpy)
li= list(range(1,11))
print(li)
print(li[0],li[1],id(li[0]),id(li[1])) # list에서 각요소들은 주소가 다르다
print(li*10) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4,...] 연산x 반복o



print()
num_arr= np.array(li)
print(num_arr[0],num_arr[1],id(num_arr[0]),id(num_arr[1])) # 각 요소들의 주소가 같음
print(num_arr * 10) # 요소에 각각 연산 [ 10  20  30  40  50  60 ...]
print('타입:',type(num_arr),num_arr.dtype, '배열의 모양(return타입 튜플) :',num_arr.shape, '차원 :',num_arr.ndim,'요소의 갯수 :',num_arr.size)
print(num_arr[1],'',num_arr[1:5]) # 슬라이싱 가능

print('------------')
b = np.array([[1,2,3],[4,5,6]]) # 행렬화
print(b)
print(b.ndim)
print(b[0],b[0][0],b[[0]])

c = np.zeros((2,2)) # 0으로 2행 2열짜리 배열화
print(c)

d = np.ones((2,2)) # 1로 2행 2열짜리 배열화
print(d)

e = np.full((2,2), fill_value=7) # 7로 2행 2열짜리 배열화
print(e)

f = np.eye(3) # 주 대각이 1씩 들어간 3행 3열짜리 배열화 (주대각이 1인 단위행렬)
print(f)

print()
np.random.seed(0)

print(np.random.rand(5)) # 균등분포
print(np.mean(np.random.rand(5)))

print(np.random.randn(5)) # 정규분포
print(np.mean(np.random.randn(5)))

print()
print(list(range(1,10))) # list 
print(np.arange(10)) # <class 'numpy.ndarray'>

print()
a = np.array([1,2,3,4,5]) # list를 넣어주면
print(a[1:4]) # <class 'numpy.ndarray'>로 변환 [2 3 4]
print(a[1:4:2])
print(a[1:])
print(a[-4])

b = a
print(a)
print(b)
b[0] = 33
print(a) # a도 바뀌어있음 (주소를 치환했기 때문에)
print(b)
c = np.copy(a) # a를 복사했기 때문에 객체가 따로 만들어진 것임
c[0] = 77
print(a) # 그렇기 때문에 a는 안변함
print(c)

print('----------------')
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:])
print(a[0],'0행0열:',a[0][0],'2차원형식을 갖춘0행:',a[[0]])
print(a[[0][0]],a[0,0])
print(a[1,0:2])

print()
print(a)
b = a[:2,1:3] # 결국 주소를 치환한 것이기 때문에
print(b)
b[0,0]=88
print(b)
print(a) # a도 바뀌어있다

print()
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
r1 = a[1,:] # 2번째 행의 모든열
r2 = a[1:2,] # a의 1이상 2미만 요소의(2행) 모든값?
print(r1, r1.shape,'1차원') # 1차원  # 인덱싱을 했기 때문에 1차원
print(r2, r2.shape,'2차원') # 2차원  # 슬라이싱을 했기 때문에 2차원, 슬라이싱만으로도 차원을 조절할 수 있다. (슬라이싱은 틀을 유지한채로 요소를 뽑아내기 때문)

print()
c1 = a[:,1] # 전체행의 1열
c2 = a[:,1:2] # 전체행의 1열,2열
print(c1, c1.shape)
print(c2, c2.shape)

print()
bool_idx = (a > 5)
print(bool_idx)
print(a[bool_idx]) # 배열안에 boolean을 넣어도 된다
print(a[a > 5])