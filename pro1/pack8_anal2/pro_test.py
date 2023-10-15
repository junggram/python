# 추론통계 분석 중 비율검정
# - 비율검정 특징
# : 집단의 비율이 어떤 특정한 값과 같은지를 검증.
# : 비율 차이 검정 통계량을 바탕으로 귀무가설의 기각여부를 결정.

# # one-sample : ( 비교할 비율이 제시된 경우 )
# A회사에는 100명 중에 45명이 흡연을 한다. 국가 통계를 보니 국민 흡연율은 35%라고 한다
# 비율이 같냐? 비율의 동일여부를 검정하시오

# 귀무 : A회사의 흡연율과 국민흡연율의 비율이 같다
# 대립 : A회사의 흡연율과 국민흡연율의 비율이 같지 않다

import numpy as np
from statsmodels.stats.proportion import proportions_ztest  # 비율 분석

count = np.array([45]) # 비율   45명
nobs = np.array([100]) # 관찰값 100명

z,p = proportions_ztest(count=count,
                         nobs=nobs,
                          value=0.35) # value는 비교값 ( 국민 흡연율 )

print('z:{},p:{}'.format(z,p)) 
# p:[0.04442318] > 0.05 대립채택, A회사의 흡연율과 국민흡연율의 비율이 같지 않다


# # two-sample : ( 비교할 비율이 제시되지 않은 경우 )
# A회사 사람들 300명 중 100명이 커피를 마시고, B회사 사람들 400명 중 170명이 커피를 마셨다, 비율이 같냐?
# 귀무 : 비율이 같다
# 대립 : 비율이 다르다

count = np.array([100,170]) 
nobs = np.array([300,400])

z,p = proportions_ztest(count=count,
                         nobs=nobs,
                          value=0) # 비율이 없으면 value는 0으로 비교

print('z:{},p:{}'.format(z,p))
#  p:0.01367 < 0.05 대립채택, 비율이 다르다