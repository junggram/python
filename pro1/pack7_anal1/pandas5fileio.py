#pandas로 파일 읽기 및 저장
import pandas as pd
from pandas.tests.frame.methods.test_sort_values import ascending

df = pd.read_csv("../testdata/ex1.csv")
print(df,type(df))

print()

df = pd.read_table("../testdata/ex1.csv", sep=',', # 텍스트 파일을 읽어오는 read_table 로 읽어올 때는 구분자(sep)를 부여해줘야함 
                   skipinitialspace=True           # 공백 없애기 skipinitialspace=True
                   ) 

print(df.info(),type(df))

print()
df = pd.read_csv("../testdata/ex2.csv", header=None,
                 names=list('korea')
                 )
print(df)

print()
df = pd.read_csv("../testdata/ex3.txt",  # txt파일은 csv로 읽을 수 있음
                 sep='\s+',              # sep=정규표현식 
                 skiprows=[1,3]          # 1,3행 제외
                 ) 
print(df)

print()
# df = pd.read_fwf("../testdata/data_fwt.txt", header=None)
df = pd.read_fwf("../testdata/data_fwt.txt", header=None,
                 widths=(10,3,5),                           # widths=(10,3,5) 붙어서 나오는 글자를 나누기
                 names=('date','name','price')
                 ) 
print(df)
print(df['date'].head(3))

print('chunk : 파일의 크기가 큰 경우 일정 행 단위로 끊어 읽기') # * 알아두자~ *
test= pd.read_csv("../testdata/data_csv2.csv", header=None,
                  chunksize=3                               # 3개씩 끊어읽기 (메모리 절약 차원)
                  ) 
print(test)
print('------')
for piece in test:
    print(piece.sort_values(by=2, ascending=True))          # 2번째 열 내림차순 정렬(청크 단위)
    

print('---- DataFrame을 파일로 저장 ----')
items = {'apple':{'count':10, 'price':1500}, 'orange':{'count':5, 'price':1000}}
df = pd.DataFrame(items)
print(df)

df.to_clipboard() # 클립 보드에 저장
print(df.to_html()) # html로
print(df.to_csv()) # csv로 
print(df.to_json()) # json으로

print()
df.to_csv('result1.csv')
df.to_csv('result2.csv', index=False, sep=',')
df.to_csv('result3.csv', index=False, header=False, sep=',')

data = df.T
print(data)
#data.to_csv('result4.csv', index=False, sep=',')

print('----- excel파일 읽기/저장하기 -----')
writer=pd.ExcelWriter('result5.xlsx', engine='xlsxwriter') # writer 작성
df.to_excel(writer, sheet_name='test') # df를 엑셀로
writer.save() # 저장

print()
myexcel = pd.read_excel('result5.xlsx', sheet_name='test')
print(myexcel)


# 문제
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv")

# 1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
#     cut() 함수 사용
#     bins = [1, 20, 35, 60, 150]
#     labels = ["소년", "청년", "장년", "노년"]
print('1번')
bins = [1, 20, 35, 60, 150]
Survived = pd.cut(df['Age'],bins, labels = ["소년", "청년", "장년", "노년"])
print(Survived.describe(),'인포')
print(pd.value_counts(Survived))

# 2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
#
#     df.pivot_table()
#     index에는 성별(Sex)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
#     출력 결과 샘플1 :
print('2번')
print(df.pivot_table(values=['Survived'],index=['Sex'], columns=['Pclass']))
print('3번')
df=df.pivot_table(values=['Survived'],
                  index=['Sex',Survived],
                  columns=['Pclass'],)*100
print(df.round(2))

print('-------------------------------------------')
# pandas 문제 4)
#   https://github.com/pykwon/python/tree/master/testdata_utf8
#   1) human.csv 파일을 읽어 아래와 같이 처리하시오.
#       - Group이 NA인 행은 삭제
#       - Career, Score 칼럼을 추출하여 데이터프레임을 작성
#       - Career, Score 칼럼의 평균계산

human_df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')
print(human_df.head(2))

human_df = human_df.rename(columns=lambda x: x.strip())  # 데이터 앞 공백 제거
print(human_df.head(2))

human_df['Group'] = human_df['Group'].str.strip()  # Group 앞 공백 제거
print(human_df.head(2))

human_df = human_df[human_df['Group']!='NA']
print(human_df.head(5),"\n")

cs_df = human_df[human_df.columns[2:4]] # Career, Score 칼럼의 평균계산
print(cs_df.head(5),"\n")
print(cs_df.mean())

print('--------------')
# 2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
#      - 파일 정보 확인
#      - 앞에서 3개의 행만 출력
#      - 요약 통계량 보기
#      - 흡연자, 비흡연자 수를 계산  : value_count()
#      - 요일을 가진 칼럼의 유일한 값 출력  : unique()
#         결과 : ['Sun' 'Sat' 'Thur' 'Fri']
    
tips_df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tips.csv')
print(tips_df.info())
print(tips_df.head(3))
print(tips_df.describe())
print(pd.value_counts(tips_df['smoker']))
print(pd.unique(tips_df['day']))