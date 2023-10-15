# 세 개 이상의 모집단에 대한 가설검정 – 분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 
# 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고
# 요인에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.

# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에
# 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
# * 서로 독립인 세 집단의 평균 차이 검정

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv'

# 귀무 : 세가지 교육방법에 따른 시험점수의 차이가 없다
# 대립 : 세가지 교육방법에 따른 시험점수의 차이가 있다

data = pd.read_csv('../testdata/three_sample.csv')

print(data.head(3))
print(data.shape)
print(data.describe()) # 이상치가 있는것을 확인했다

# plt.boxplot(data['score'])  # 2개의 이상치를 확인
# plt.hist(data['score'])
# plt.show()

data = data.query('score <= 100') # 이상치 제거
print(data.shape) # (78, 4)

result = data[['method','score']] # 교육방법 1
m1 = result[result['method']==1]
m2 = result[result['method']==2]
m3 = result[result['method']==3]

score1 = m1['score']
score2 = m2['score']
score3 = m3['score']

print(score1[:3,])
print(score2[:3,])
print(score3[:3,])

# 정규성 (만약 과반수 이상의 데이터가 정규성을 만족하면 anova, 아니면 kruskal-wallis test 사용
# 한개의 표본이 같은 분포를 따르는지 확인
print('%.3f'%stats.shapiro(score1).pvalue) # 0.175 > 0.05 , 정규성 만족
print('%.3f'%stats.shapiro(score2).pvalue) # 0.332 > 0.05 , 정규성 만족
print('%.3f'%stats.shapiro(score3).pvalue) # 0.116 > 0.05 , 정규성 만족 

# 두개의 표본이 같은 분포를 따르는지 확인
print('%.3f'%stats.ks_2samp(score1, score2).pvalue) # 0.310 > 0.05 , 정규성 만족
print('%.3f'%stats.ks_2samp(score2, score3).pvalue) # 0.772 > 0.05 , 정규성 만족
print('%.3f'%stats.ks_2samp(score1, score3).pvalue) # 0.716 > 0.05 , 정규성 만족


# 등분산성 ( 만족하지 않으면 welch_anova test 사용 )
print('%.3f'%stats.levene(score1,score2,score3).pvalue) # 0.113 > 0.05 , 등분산성 만족
print('%.3f'%stats.fligner(score1,score2,score3).pvalue) # 0.108 > 0.05 , 등분산성 만족
print('%.3f'%stats.bartlett(score1,score2,score3).pvalue) # 0.153 > 0.05 , 등분산성 만족

# 참고 : 등분산성을 만족하지 않는 경우 대안 = 데이터를 정규화, 표준화, 자연log를 붙이는 방법

print('교육방법별 건수 : 교차표')
data2 = pd.crosstab(index=data['method'],columns=['count'])
data2.index = ['방법1','방법2','방법3']
print(data2)

print('교육방법별 만족여부 건수 : 교차표')
data3 = pd.crosstab(index=data['method'],columns=data['survey'])
data3.index = ['방법1','방법2','방법3']
data3.columns = ['만족','불만족']
print(data3)

# anova 진행
import statsmodels.api as sm

#독립변수:1 종속변수:1
reg = ols('score ~ method', data = data).fit()
table = sm.stats.anova_lm(reg, typ=1) # anova 테스트 typ = 2 를 보통 많이씀
print(table) # 분산 분석표 출력 # F 값은 = 27.980888 / 228.922922 ( method의 mean_sq / Residual의 mean_sq )
# 해석 : p-value 0.727597 > 0.05 귀무 채택

'''#독립변수:2, 종속변수:1  
reg2 = ols('score ~ C(method + survey)', data = data).fit()
table2 = sm.stats.anova_lm(reg2, typ=2) 
print(table2) # 분산 분석표 출력'''
#-------------------------------

print('''사후 검정 : 그룹 전체의 평균에 차이가 있음을 알려주나
                각 그룹 사이의 평균의 차이는 알려주지 않는다.
                그래서 사후검정 수행 ''')
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

print('평균 :',np.mean(score1),' ',np.mean(score2),' ',np.mean(score3) )  
     # 평균 : 67.38461538461539   68.35714285714286   68.875
     
# 평균점수에 차이가 없다고 검정됐고 귀무채택이 됐다
# post hoc test (사후 검정)

tukeyResult = pairwise_tukeyhsd(endog=data['score'], groups=data['method'])
print(tukeyResult)
#===============================================================================

# group1 group2 meandiff p-adj   lower   upper  reject    * reject 가 True가 나오면
# ----------------------------------------------------      유의미한 차이가 있다는 것이다
#      1      2   0.9725 0.9702 -8.9458 10.8909  False
#      1      3   1.4904 0.9363 -8.8183  11.799  False
#      2      3   0.5179 0.9918 -9.6125 10.6483  False
# ----------------------------------------------------

#===============================================================================

# 시각화
tukeyResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()