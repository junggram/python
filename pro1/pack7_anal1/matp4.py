# 자전거 공유 시스템 분석용
# kaggle 사이트의 Bike Sharing in Washington D.C. Dataset를 편의상 조금 변경한 dataset을 사용함
'''
columns : 
 'datetime', 
 'season'(사계절:1,2,3,4), 
 'holiday'(공휴일(1)과 평일(0)), 
 'workingday'(근무일(1)과 비근무일(0)), 
 'weather'(4종류:Clear(1), Mist(2), Snow or Rain(3), Heavy Rain(4)), 
 'temp'(섭씨온도), 'atemp'(체감온도), 
 'humidity'(습도), 'windspeed'(풍속), 
 'casual'(비회원 대여량), 'registered'(회원 대여량), 
 'count'(총대여량) 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False #tick이 음수일 때 깨짐 방지

train = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/data/train.csv', 
                    parse_dates = ['datetime']) # 데이터 type을 바꿈 [ dates => datetime ]
print(train.head(3))
print(train.shape)
print(train.columns)
print(train.info())

print(train.temp.describe()) # 
print(train.isnull().sum()) # null인 칼럼이 있는지 확인

# null이 포함된 칼럼 확인용 시각화
# pip install missingno

# import missingno as msno
# msno.matrix(train, figsize=(12,5))
# plt.show()

# 연월일 시분초를 별도 칼럼으로 추가
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second

print(train.head(2))
print(train.columns)

# 대여량 시각화 (bar)

figure,(ax1,ax2,ax3,ax4) = plt.subplots(nrows=1,ncols=4)
figure.set_size_inches(15,5)

sns.barplot(data = train, x='year', y='count', ax=ax1) # 막대그래프
sns.barplot(data = train, x='month', y='count',ax=ax2)
sns.barplot(data = train, x='day', y='count',ax=ax3)
sns.barplot(data = train, x='hour', y='count',ax=ax4)
ax1.set(ylabel='Count', title='연도별 대여량')
ax2.set(ylabel='Count', title='월별 대여량')
ax3.set(ylabel='Count', title='일별 대여량')
ax4.set(ylabel='Count', title='시간별 대여량')
plt.show()

# 대여량 시각화 (boxplot)

figure, axes = plt.subplots(nrows=2,ncols=2)
figure.set_size_inches(15,5)

sns.boxplot(data = train, y='count', orient='v', ax = axes[0][0])
sns.boxplot(data = train, y='count', x='season', orient='v', ax = axes[0][1]) 
sns.boxplot(data = train, y='count', x='hour', orient='v', ax = axes[1][0])
sns.boxplot(data = train, y='count', x='workingday', orient='v', ax = axes[1][1])
axes[0][0].set(ylabel='대여량', title='대여량')
axes[0][1].set(xlabel='계절별',ylabel='대여량', title='계절별 대여량')
axes[1][0].set(xlabel='시간별',ylabel='대여량', title=' 시간별 대여량')
axes[1][1].set(xlabel='근무여부별',ylabel='대여량', title=' 근무여부별대여량')
plt.show()

# 산점도의 일종으로 rugplot - temp, windspeed, humidity

fig,(ax1,ax2,ax3) = plt.subplots(ncols=3)
fig.set_size_inches(10,5)

sns.rugplot(x='temp',y='count',data=train, ax = ax1)
sns.rugplot(x='windspeed',y='count',data=train, ax = ax2)
sns.rugplot(x='humidity',y='count',data=train, ax = ax3)
plt.show()