# 색인
import pandas as pd
import numpy as np

# Series의 재 색인
data = pd.Series([1,3,2], index=(1,4,2)) # index는 list, tuple, set 가능
print(data)

# 순서를 재 배치
data2 = data.reindex((1,2,4))
print(data2)

print()
data3 = data2.reindex([0,1,2,3,4,5])
print(data3) # 대응값이 없는 인덱스에는 NaN이 됨

print() # NaN(결측값) 채우기

data3 = data2.reindex([0,1,2,3,4,5], method='ffill') # NaN의 이전값으로 NaN을 채움
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='pad') # 위와 같음
print(data3)

data3 = data2.reindex([0,1,2,3,4,5], method='bfill') # NaN의 이후값으로 NaN을 채움
print(data3)
data3 = data2.reindex([0,1,2,3,4,5], method='backfill') # 위와 같음
print(data3)

print('------------------------')
df = pd.DataFrame(np.arange(12).reshape(4,3),  # 예시로 0~11까지의 숫자로 4행 3열짜리 배열을 만든다
                  index=['1월', '2월','3월','4월'], # 인덱스 부여
                  columns=['강남','강북','서초']) # 칼럼 부여
print(df)
print(df['강남'])
print(df['강남'] > 3) # True, False만 출력
print(df[df['강남'] > 3]) # 조건이 True인 '행들을' 출력

print()
print('------- 슬라이싱 관련 method(복수 인덱싱) :  loc - 라벨 지원, iloc - 숫자 지원 ----------')
print('--loc--')
print(df.loc['3월', :]) # '3월 행의 모든 열 값'
print(df.loc[:'2월']) # 2월행 이하의 모든 값
print(df.loc[:'2월', '서초']) # 2월행 이하의 행의 서초 열만 출력    

print('--iloc--')
print(df.iloc[2]) # 3번째 행의 모든 열의 값 
print(df.iloc[2,:]) # 3번째 행의 모든 열의 값 
print(df.iloc[:3]) # 3행 까지의 모든 열의 값
print(df.iloc[:3,2]) # 3행 까지의 2번째 열의 값
print(df.iloc[1:3, 1:3]) # 2,3행의 2,3열의 값

print('산술 연산')
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([4,5,6,7], index=['a','b','d','c'])
print(s1)
print(s2)
print(s1+s2) # 인덱스가 대응되는 값들만 연산이됨  # d = NaN
print(s1.add(s2)) # add(+), sub(-), mul(*), div(/)

print()
df1 = pd.DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'),index=['서울','대전','부산'])
df2 = pd.DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'),index=['서울','대전','제주','목포'])
print(df1)
print(df2)
print(df1+df2) # 인덱스가 대응되는 값들만 연산이됨  # 목포, 부산, 제주 = NaN
print(df1.add(df2)) # 인덱스가 대응되는 값들만 연산이됨  # 목포, 부산, 제주 = NaN
print(df1.add(df2, fill_value=0)) # NaN은 특정 값으로 채울때 fill_value()

print('---')
seri=df1.iloc[0]
print(df1)
print(seri)
print(df1 - seri) # 시리즈의 색인을 dataframe에 맞춤 (브로드캐스팅)

print('---기술적 통계와 관련된 메소드(함수)---')
# 기술적 통계와 관련된 메소드(함수)
df = pd.DataFrame([[1.4,np.nan],[7,-4.5],[np.NaN,None], [0.5,-1]],columns=['one','two'])
print(df)
print(df.drop(1))
print(df.isnull()) # 결측치 탐지 ( boolean 리턴 )
print(df.notnull()) # 위와 반대
print()
print(df.dropna()) # NaN을 탐지해서 모두 지움 (하나라도 NaN이면 지움)
print(df.dropna(how='any')) # NaN을 탐지해서 모두 지움 (하나라도 NaN이면 지움)
print(df.dropna(how='all')) # NaN을 탐지해서 모두 지움 (모두 NaN이면 지움)
print(df.dropna(axis='rows')) # NaN이 포함된 행을 지움
print(df.dropna(axis='columns')) # NaN이 포함된 열을 지움
print(df.dropna(axis='columns', how='all')) # 응용 : 모든 열이 NaN인 열을 지움

print()
print(df.fillna(0)) # 결측치를 0 또는 평균등의 값으로 대체
print(df.fillna(method='ffill')) # 결측치를 앞의 값으로 대체
print(df.fillna(method='bfill')) # 결측치를 뒤의 값으로 대체
print(df.dropna(subset=['one'])) # one열 중에서 NaN이 있는 행을 지움

print('---')
print(df)
print(df.sum()) # NaN은 연산에서 제외
print(df.sum(axis=0)) # 열의 합
print(df.sum(axis=1)) # 행의 합
print(df.mean(axis=1)) # 행의 평균
print(df.mean(axis=1,skipna=True))
print(df.mean(axis=1,skipna=False)) # NaN를 연산에 포함하기 때문에 하나라도 NaN이면 결과가 NaN
print()
print(df.describe()) # 요약 통계량 
print(df.info()) # 구조 확인

# pandas 문제 1)
#
#   a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
#
#      np.random.randn(9, 4)
#
#   b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
#
#   c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
print('---1번---')

np.random.seed(1)
testdf=pd.DataFrame(np.random.randn(9,4), columns=['No1','No2','No3','No4'])
print(testdf)
print(testdf.mean(axis=0))

print('--2번--')
# a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.
#
# b) c row의 값을 가져오시오.
#
# c) a, d row들의 값을 가져오시오.
#
# d) numbers의 합을 구하시오.
#
# e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.
#
# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.
#
# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.

import pandas as pd
from pandas import Series, DataFrame

testdf2=pd.DataFrame(np.arange(10,50,10).reshape(4,1), columns=['numbers'], index=['a','b','c','d'])
#print(testdf2)
print(testdf2.loc['c'])
print(testdf2.loc[['a','d']])
print(testdf2.sum(axis=0)) # print(testdf2.numbers.sum())
print(testdf2*testdf2)

'''data = {
    'numbers':[10,20,30,40],
    'float':[1.5,2.5,3.5,4.5]
}
testdf2=pd.DataFrame(data, index=['a','b','c','d'])
print(testdf2)
val= Series(['길동','오정','팔계','오공'],index=['d','a','b','c'])
testdf2['names']=val
print(testdf2)'''

testdf2['floats']=[1.5,2.5,3.5,4.5]
print(testdf2)

testdf2['flower']=pd.Series(['장미','수국','개나리',None],
                           index = ['a','b','c','d'])
print(testdf2)
print(testdf2.info()) # 구조 확인

testdf2['names']=pd.Series(['길동','오정','팔계','오공'],
                           index = ['d','a','b','c'])
print(testdf2)