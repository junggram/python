# 어느 음식점 매출 자료와 날씨 자료를 활용하여 강수 여부에 따른 매출액 평균의 차이를 검정

# 귀무 : 강수 여부에 따른 음식점 매출액의 평균에 차이가 없다
# 대립 : 강수 여부에 따른 음식점 매출액의 평균에 차이가 있다

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 매출액
sales = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv',dtype={'YMD' : 'object'}) # 불러올 때 dtype을 바꿀 수 있음
print(sales.head(3),sales.info())

print()

# 날씨 정보
weather = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv')
# 두 데이터를 병합하기위해 날짜를 사용  ->  weather의 날짜정보를  2018-06-01 => 20180601 으로 변환
weather['tm']=weather['tm'].map(lambda x:x.replace('-',''))
print(weather.head(3),weather.info())


frame = sales.merge(weather, how='left', left_on='YMD', right_on='tm') # 날짜를 기준으로 병합
print(frame, len(frame))  # 328개의 데이터
print(frame.columns) # (['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes'])
data = frame.iloc[:,[0,1,7,8]] # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data)

print(data.isnull().sum()) # 결측치 검정 => 0
print('두 집단 간의 매출액 평균 검정 : t-test')

data['rain_yn'] = (data['sumRn'] > 0).astype(int) # 비가 오면 1, 안오면 0
print(data.head(3))

# boxplot으로 강수 여부에 따른 매출액 시각화
sp = np.array(data.iloc[:,[1,4]])
# print(sp)
tg1 = sp[sp[:,1]==0, 0] # 비가 안오는 그룹의 매출액
tg2 = sp[sp[:,1]==1, 0] # 비가 오는 그룹의 매출액

# plt.boxplot([tg1, tg2], meanline=True, showmeans=True, notch=True)
# plt.show()
# print('평균은', np.mean(tg1), np.mean(tg2)) # 평균은 761040.25,  757331.52

# 정규성 확인
print(stats.shapiro(tg1).pvalue) # 0.056  # 정규성 만족  >  0.05
print(stats.shapiro(tg2).pvalue) # 0.882  # 정규성 만족

# 등분산성 확인
print(stats.levene(tg1, tg2).pvalue) # 0.71 # 등분산성 만족  >  0.05

print(stats.ttest_ind(tg1, tg2)) # statistic=0.10109828602924716, pvalue=0.919534587722196
# 해석 : p-value:0.91953 > 0.05 이므로 귀무가설 채택, 강수 여부에 따른 매출액의 평균에 차이가 없다

'''
data1=data[data['sumRn']==0]['AMT']
data2=data[data['sumRn']!=0]['AMT']
# print(data1)
# print(data2)
print(data1.mean(), data2.mean()) # 평균은 761040.25,  757331.52

# data1=data1['AMT']
# data2=data2['AMT']
# print(data1)
# print(data2)

import seaborn as sns

sns.histplot(data1, kde = True, color='red')
sns.histplot(data2, kde = True, color='green')
plt.show()

result = stats.ttest_ind(data1, data2) # 정규성 만족, 등분산성 만족
print('t-value:%.5f, p-value:%.5f'%result) # t-value:0.10110, p-value:0.91953
# 해석 : p-value:0.91953 > 0.05 이므로 귀무가설 채택 
'''