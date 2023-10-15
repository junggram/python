# 어느 음식점 매출 자료와 날씨 자료를 활용하여 온도(추움, 보통, 더움)에 따른 매출액 평균의 차이를 검정

# 귀무 : 온도에 따른 음식점 매출액의 평균에 차이가 없다
# 대립 : 온도에 따른 음식점 매출액의 평균에 차이가 있다

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
print(data.head(3))

# 일별 최고온도(maxTa)를 구간설정을 해서 연속형을 범주형 변수를 추가

print(data['maxTa'].describe())

data['Ta_gubun'] = pd.cut(data['maxTa'],bins=[-5,8,24,37], labels=[0,1,2])
print(data.head(3))
print(data.isnull().sum()) # 결측치 확인

# 세 그룹의 매출액으로 정규성, 등분산성
x1 = np.array(data[data['Ta_gubun']==0].AMT)
x2 = np.array(data[data['Ta_gubun']==1].AMT)
x3 = np.array(data[data['Ta_gubun']==2].AMT)
print(x1[:3])
print(x2[:3])
print(x3[:3])

# 정규성
print(stats.ks_2samp(x1, x2).pvalue) # 9.28938415079017e-09 < 0.05  # 정규성 만족x
print(stats.ks_2samp(x2, x3).pvalue) # 1.4133139103478243e-13
print(stats.ks_2samp(x3, x1).pvalue) # 1.198570472122961e-28

# 등분산성
print(stats.levene(x1,x2,x3).pvalue) # 0.039 < 0.05 # 등분산성 만족x

print('온도별 매출액 평균')
spp = data.loc[:,['AMT','Ta_gubun']]
print(spp.groupby('Ta_gubun').mean())
print(pd.pivot_table(spp, index=['Ta_gubun'], aggfunc='mean'))

# anova 진행
sp = np.array(spp)
print(sp[:3])
group1 = sp[sp[:,1]==0,0]
group2 = sp[sp[:,1]==1,0]
group3 = sp[sp[:,1]==2,0]

# # 데이터 분포 시각화
# plt.boxplot([group1,group2,group3],showmeans = True)
# plt.show()

print()
print(stats.f_oneway(group1,group2,group3)) # pvalue=2.360737101089604e-34
# 해석 : pvalue=2.360737101089604e-34 < 0.05 이므로, 귀무 가설 기각
# 음식점 매출액의 평균은 온도에 영향이 있다.

# 정규성을 만족하지 않으므로
print(stats.kruskal(group1,group2,group3))
# statistic=132.7022591443371, pvalue=1.5278142583114522e-29


# 등분산성을 만족하지 않으므로 (welch_anova)
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(data=data, dv='AMT', between='Ta_gubun'))

#      Source  ddof1     ddof2           F         p-unc       np2
# 0  Ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038

print('----------------------------------------')

# 각 지역의 평균 차이가 궁금 => 사후 검정

from statsmodels.stats.multicomp import pairwise_tukeyhsd
# post hoc test (사후 검정)

tukeyResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['Ta_gubun'], alpha = 0.05)
print(tukeyResult)
#===============================================================================

# =================================================================
# group1 group2   meandiff   p-adj    lower        upper     reject
# -----------------------------------------------------------------
#      0      1 -214255.4486   0.0  -296755.647 -131755.2503   True
#      0      2 -478651.3813  -0.0 -561484.4539 -395818.3088   True
#      1      2 -264395.9327  -0.0 -333326.1167 -195465.7488   True
# -----------------------------------------------------------------

#===============================================================================

# 시각화
tukeyResult.plot_simultaneous(xlabel='AMT', ylabel='Ta_gubun')
plt.show()