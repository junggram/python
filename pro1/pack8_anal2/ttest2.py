# 두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
# * 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.

from scipy import stats
import pandas as pd
from numpy import average
# 실습) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

# 귀무 : 남녀 두 집단 간 파이썬 시험의 차이가 없다
# 대립 : 남녀 두 집단 간 파이썬 시험의 차이가 있다

print(average(male), ' ',average(female)) # 83.8   72.24
print(83.8 - 72.24) # 11.56

two_sample = stats.ttest_ind(male, female) # 두개의 표본에 대한 t-test 실시
print(two_sample)
# 해석 : p-value=0.252507 > 0.05 이므로 귀무가설 채택

print('----------------------------------------------')

# 실습) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv
data = pd.read_csv('../testdata/two_sample.csv')
print(data.head(3),len(data))

# 귀무 : 두가지 교육방법에 따른 평균시험 점수에 대한 차이가 없다
# 대립 : 두가지 교육방법에 따른 평균시험 점수에 대한 차이가 있다


ms = data[['method','score']]
# print(ms)

# 교육방법 별로 분류
m1 = ms[ms['method'] == 1]
m2 = ms[ms['method'] == 2]

score1 = m1['score'] # 1번 방법의 점수
score2 = m2['score'] # 2번 방법의 점수

print(score1)
print(score2)

sco1 = score1.fillna(score1.mean())
sco2 = score2.fillna(score1.mean()) # NaN을 평균으로 대체

print(sco1)
print(sco2)

# 정규성 검정
import matplotlib.pyplot as plt
import seaborn as sns

# sns.histplot(sco1, kde = True, color='red')
# sns.histplot(sco2, kde = True, color='green')
# plt.show()

print(stats.shapiro(sco1).pvalue) # p-value만 뽑아서 볼 수 있다     # 0.367990 > 0.05 = 정규성 만족
print(stats.shapiro(sco2).pvalue)                               # 0.717721 > 0.05 = 정규성 만족

# 등분산성
print(stats.levene(sco1, sco2).pvalue) # 0.43483  >  0.05  등분산성 만족
print(stats.fligner(sco1, sco2).pvalue) # 0.37514
print(stats.bartlett(sco1, sco2).pvalue) # 0.26760

result = stats.ttest_ind(sco1, sco2) # 정규성 만족, 등분산성 만족
print('t-value:%.5f, p-value:%.5f'%result) # t-value:-0.17337, p-value:0.86309
# 해석 : p-value:0.86309 > 0.05 이므로 귀무가설 채택

print('--------참고---------')
result = stats.ttest_ind(sco1, sco2,equal_var=True) # 정규성 만족, 등분산성 만족   #  equal_var=True 기본값 (생략되어있음)
print('t-value:%.5f, p-value:%.5f'%result)

result = stats.ttest_ind(sco1, sco2,equal_var=False) # 정규성 만족, 등분산성 불만족
print('t-value:%.5f, p-value:%.5f'%result)

print()
# result2 = stats.wilcoxon(sco1, sco2)  # 정규성을 만족하지 않은 경우
result2 = stats.mannwhitneyu(sco1, sco2)
print('t-value:%.5f, p-value:%.5f'%result2)