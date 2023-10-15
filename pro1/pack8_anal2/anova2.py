# 일원분산분석으로 평균차이 검정 : 한개의 요인에 따른 여러 개의 집단으로 데이터가 구성됨

# 강남구에 있는 GS편의점 3개 지역 알바생의 급여에 대한 평균 차이 검정을 실시

# 귀무 : 강남구에 있는 GS편의점 알바생의 급여에 대한 평균 차이가 없다
# 대립 : 강남구에 있는 GS편의점 알바생의 급여에 대한 평균 차이가 있다

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import urllib.request

url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt'
# data = pd.read_csv(url, header=None)  # 판다스로 읽어옴 : dataframe으로
# print(data.head())
# print(data.describe())

data = np.genfromtxt(urllib.request.urlopen(url),delimiter=',') # 넘파이로 읽어옴 : matrix로 
# print(data)
# print(data[:3],type(data))

# 세 지역 급여 평균 확인
gr1 = data[data[:,1]==1,0]
gr2 = data[data[:,1]==2,0]
gr3 = data[data[:,1]==3,0]
print('gr1 :',gr1.mean()) # 316.625
print('gr2 :',gr2.mean()) # 256.44444444444446
print('gr3 :',gr3.mean()) # 278.0    # 차이 ? 

# 정규성 검증
print(stats.shapiro(gr1).pvalue) # 0.333 > 0.05 만족
print(stats.shapiro(gr2).pvalue) # 0.656
print(stats.shapiro(gr3).pvalue) # 0.832

# 등분산성 검증
print(stats.levene(gr1,gr2,gr3).pvalue) # 0.0458 < 0.05 불만족 but 별 차이가 안난다 (그냥 작업해도됨) : welch_anova를 사용함
print(stats.bartlett(gr1,gr2,gr3).pvalue) # 0.350 > 0.05 만족

# # 데이터의 퍼짐 정도 시각화
# plt.boxplot([gr1,gr2,gr3],showmeans=True)
# plt.show()

# 일원분산분석 방법 1 : anova_lm
df = pd.DataFrame(data, columns=['pay','group'])
print(df.head(3))

lmodel = ols('pay ~ C(group)',data=df).fit()  # 선형회귀모델 작성
                                              # python에서 데이터 타입이 범주형이라면 C(  ) 를 둘러줘야한다
                                              # R과 다름
print(anova_lm(lmodel,typ=1))
# 해석 : p-value 0.0435 < 0.05 이므로, 귀무 가설 기각, 평균의 차이가 있다


# 일원분산분석 방법 2 : f_oneway()
f_sta, pvalue = stats.f_oneway(gr1,gr2,gr3)
print('f통계랑 :', f_sta) # 3.711
print('유의확률 :', pvalue) # 0.043

# 각 지역의 평균 차이가 궁금 => 사후 검정

from statsmodels.stats.multicomp import pairwise_tukeyhsd
     
# 평균급여에 차이가 있다고 검정됐고 귀무채택이 됐다
# post hoc test (사후 검정)

tukeyResult = pairwise_tukeyhsd(endog=df['pay'], groups=df['group'])
print(tukeyResult)
#===============================================================================

# ======================================================
# group1 group2 meandiff p-adj    lower    upper  reject
# ------------------------------------------------------
#    1.0    2.0 -60.1806 0.0355  -116.619 -3.7421   True
#    1.0    3.0  -38.625 0.3215 -104.8404 27.5904  False
#    2.0    3.0  21.5556 0.6802  -43.2295 86.3406  False
# ------------------------------------------------------

#===============================================================================

# 시각화
tukeyResult.plot_simultaneous(xlabel='pay', ylabel='group')
plt.show()
