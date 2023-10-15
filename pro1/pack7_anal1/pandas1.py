#Pandas
#-고수준의 자료구조(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 자료구조 및 함수를 제공한다.
#-NumPy의 고성능 배열 계산 기능과 스프레드시트
#-SQL과 같은 RDMBS의 유연한 데이터 조작 기능을 갖고 있다.
#-세련된 인덱싱 기능으로 쉽게 데이터를 재배치하여 집계 등의 처리를 편리하게 한다.

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
# Series는 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인을 갖는다.
obj = Series([3,7,-5,4]) # List  O
# obj = Series((3,7,-5,4)) # Tuple  O
# obj = Series({3,7,-5,4}) # Set type은 시리즈로 쓸 수 없다 (순서가 없기에 인덱싱이 불가함)
print(obj,type(obj)) # dtype: int64 <class 'pandas.core.series.Series'>

obj2 = Series([3,7,-5,4], index=['a','b','c','d']) # 생성시 인덱스 지정 가능
print(obj2)
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2)) # 순서대로 판다스함수, 넘파이함수, 파이썬함수
print(obj2.mean(), obj2.std()) # 동일하게 다른 판다스 함수도 사용가능

print(obj2.values) # List 아니고 Array type임
print(obj2.index) # index 값을 얻을수도 있음


print()
print('----인덱싱, 슬라이싱------')
print()

print(obj2[0], obj2['a'],obj2[['a']]) # 0번째로 써도 되고, 따로 인덱싱해준 문자열을 써줘도됨   # obj2[['a']] 이렇게 쓰면 'a'행을 불러옴
print(obj2[['a','b']]) # 여러 행을 불러옴 # Series type
print(obj2['a':'b']) # 범위지정해서 여러 행을 불러옴 # Series type
print(obj2[1:4])
print(obj2[[2,1]])
print(obj2>0)
print('a' in obj2) # boolean 리턴 있으면 True 없으면 False



print()
print('----dict로 Series 객체 생성------')
print()

names = {'mouse': 5000, 'keyboard': 25000, 'monitor': 350000} # dict도 순서가 없지만 key값이 있기 때문에 Series객체로 생성가능함
obj3 = Series(names)
print(obj3)

obj3.index = ['마우스', '키보드','모니터'] # 키값을 바꿀수도 있음 (인덱스 변경)
print(obj3)

print()
obj3.name='상품가격' # Series의 name을 줄 수 있음
print(obj3)


# DataFrame :
# 표 모양(2차원 형태 자료)의 자료구조로 여러 개의 칼럼을 갖는다. (Series가 모인 형태)
# 각 칼럼은 서로 다른 종류의 값을 기억할 수 있다.

df = DataFrame(obj3) # Series로 DataFrame 객체 생성.
print(df) # name이 열의 이름으로 쓰이고있음

# 같은 길이의 리스트에 담긴 dict type의 데이터를 이용해 DataFrame 객체 생성.

data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':['역삼동', '신당동', '역삼동', '역삼동', '신사동'],
    'nai':[23, 25, 33, 30, 35],
}
print(data)

frame=pd.DataFrame(data)
print(frame, '\n',type(frame))

print(frame['irum'],type(frame['irum'])) # 원하는 열만 불러낸다
print(frame.irum, type(frame.irum)) # 위와 같다 (위를 더 많이 씀)

print()
print('----열 순서 변경------')
print()
print(DataFrame(data, columns=['juso', 'irum', 'nai'])) # 열의 순서가 바뀜
print()
frame2=DataFrame(data, columns=['irum', 'juso', 'nai', 'tel'], index=['a','b','c','d','e']) # 열을 추가해서 만듬
print(frame2)

frame2['tel']='111-1111' # 모든 행에 입력
print(frame2)

val = Series(['222-2222', '333-2222', '444-2222', '555-2222'], # 덮어쓰기 이기 때문에 이전 입력한 111-1111 은 NaN 로 바뀜
             index=['b','c','d','e'] # 인덱스에 지정해서 value를 넣어줄 수도 있다
             )  # Series 객체로 만들어서 입력함
frame2['tel']= val
print(frame2)

print('---')
print(frame2.T) # 행과 열 변경 (transpose)

print(frame2.values) # 2차원으로 결과 반환
print(frame2.values[0,1]) # 0행 1열 값을 반환
print(frame2.values[0:3]) # 0~2행까지 반환

print()
frame3 = frame2.drop('d') # 행방향 삭제 # axis=0 이 생략되어있음
print(frame3)
frame4 = frame2.drop('tel', axis=1) # 열방향 삭제
print(frame4)

# index명 / 열 이름으로 정렬
print('----프레임2----')
print(frame2)
print('----행방향 내림차순----')
print(frame2.sort_index(axis=0,ascending=False))
print('----열방향 내림차순----')
print(frame2.sort_index(axis=1,ascending=False))
print()
print(frame2.rank(axis=0)) # 사전순으로 순위를 책정

print()
print(frame2['juso'].value_counts()) # 요소값의 갯수를 파악할 수 있다

print()
data={
    'juso':['강남구 역삼동','중구 신당동','강남구 대치동'],
    'inwon':[23,25,15]
}

fr = DataFrame(data)
print(fr)
result1=Series([x.split()[0] for x in fr.juso]) # 공백을 기준으로 '구'단위 [0] 를 뺌
result2=Series([x.split()[1] for x in fr.juso]) # 공백을 기준으로 '동'단위 [1] 를 뺌
print(result1)
print(result2)
print(result1.value_counts())
