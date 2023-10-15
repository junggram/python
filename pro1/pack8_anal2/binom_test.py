# 이항검정 : 결과가 두가지 값을 가지는 확률변수의 분포(이항분포)를 판단하는데 효과적
# 정규분포 연속변량, 이항분포는 이산변량

# binom test

import pandas as pd
import scipy.stats as stats

# 귀무 : 직원을 대상으로 고객대응 교육 후 고객안내 서비스 만족율은 80%이다
# 대립 : 직원을 대상으로 고객대응 교육 후 고객안내 서비스 만족율이 80%가 아니다

data = pd.read_csv('../testdata/one_sample.csv')
print(data.head(3))

print(data['survey'].unique()) # [1 0]

ctab = pd.crosstab(index = data['survey'], columns = 'count')

ctab.index = ['불만족', '만족']
print(ctab)

print('\n양측 검정 : 방향성이 없다')
x = stats.binom_test([136,14], p=0.8, alternative='two-sided') # 만족율 기준 p=0.8
print(x) 
# pvalue = 0.0006734701362867024  < 0.05  귀무 기각
# 고객안내 서비스 만족율은 80%가 아니다 차이가 있다
x = stats.binom_test([14,136], p=0.2, alternative='two-sided') # 불만족율 기준 p=0.2
print(x) 
# pvalue = 0.0006734701362867063  < 0.05  귀무 기각
# 고객안내 서비스 만족율은 80%가 아니다 차이가 있다

print('\n단측 검정 : 방향성이 있다, 크다, 적다')

# 만족 값이 클거라 가정하고 greater
x = stats.binom_test([136,14], p=0.8, alternative='greater') # 만족율 기준 p=0.8    # greater
print(x) 
# pvalue = 0.00031794019219854805  < 0.05  귀무 기각
# 고객안내 서비스 만족율은 80%보다 크다

x = stats.binom_test([14,136], p=0.2, alternative='less') # 불만족율 기준 p=0.2    # less
print(x) 
# pvalue = 0.00031794019219854924  < 0.05  귀무 기각
# 고객안내 서비스 만족율은 80%보다 크다