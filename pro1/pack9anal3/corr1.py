# 공분산 / 상관계수

import numpy as np
import matplotlib.pyplot as plt

# 공분산 예  # np.cov 공분산
print(np.cov(np.arange(1,6),np.arange(2,7))) # 2.5  양의 관계
print(np.cov(np.arange(1,6),(3,3,3,3,3)))# 0  관계없음
print(np.cov(np.arange(1,6),np.arange(6,1,-1))) # -2.5  음의 관계

print()
x = [8,3,6,6,9,4,3,9,3,4]
print('x의 평균 :',np.mean(x)) # x의 평균 : 5.5
print('x의 분산 :',np.var(x)) # x의 분산 : 5.45x

y= [6,2,4,6,9,5,1,8,4,5]
print('y의 평균 :',np.mean(y)) # x의 평균 : 5.5
print('y의 분산 :',np.var(y)) # x의 분산 : 5.45x

# plt.scatter(x, y)
# plt.show()

print('x,y의 공분산 :',np.cov(x,y)[0,1]) # x,y의 공분산 : 5.22
print('x,y의 상관계수 :',np.corrcoef(x,y)[0,1]) # x,y의 상관계수 : 0.86    # 정확히는 피어슨 상관계수

from scipy import stats

print(stats.pearsonr(x, y)) # (0.8663686463212853, 0.0011836205396685683)
print(stats.spearmanr(x, y)) # 스피어만 상관계수 Result(correlation=0.9000703207408192, pvalue=0.00038610220712161346)

# 주의 : 공분산이나 상관계수는 선형 데이터인 경우에 활용
m = [-3,-2,-1,0,1,2,3]
n = [9,4,1,0,1,4,9]
plt.scatter(m,n)
plt.show()
print('m,n의 공분산 :',np.cov(m,n)[0,1]) 
print('m,n의 상관계수 :',np.corrcoef(m,n)[0,1]) 