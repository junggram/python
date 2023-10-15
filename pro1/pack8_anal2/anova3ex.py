import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas.core.series import Series

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 차이가 없다
# 대립 : 기름의 종류에 따라 흡수하는 기름의 차이가 있다

# kind quantity
# 1 64
# 2 72
# 3 68
# 4 77
# 2 56
# 1 NaN
# 3 95
# 4 78
# 2 55
# 1 91
# 2 63
# 3 49
# 4 70
# 1 80
# 2 90
# 1 33
# 1 44
# 3 55
# 4 66
# 2 77
# kind = [1,2,3,4,2,1,3,4,2,1,2,3,4,1,2,1,1,3,4,2]
# quantity = [64,72,68,77,56,np.NaN,95,78,55,91,63,49,70,80,90,33,44,55,66,77]
# data = pd.DataFrame([kind,quantity]).T
data = pd.read_csv('기름.csv',delimiter=' ') # 구분자 꼭 기억

# print(data.head(3))
# print(data.describe())
data.columns = ['kind','quantity']
# print(data['quantity'])
data= data.fillna(data['quantity'].mean())
d1 = data[data['kind']==1]['quantity']
d2 = data[data['kind']==2]['quantity']
d3 = data[data['kind']==3]['quantity']
d4 = data[data['kind']==4]['quantity']

# 정규성 검정
print(stats.shapiro(d1).pvalue) # 0.868  # 아래도 모두 만족
print(stats.shapiro(d2).pvalue) # ...
print(stats.shapiro(d3).pvalue) # ...
print(stats.shapiro(d4).pvalue) # ...

# 등분산성 검정
print(stats.levene(d1,d2,d3,d4).pvalue) # 0.326 만족

print()

# 검정
import statsmodels.api as sm
from statsmodels.formula.api import ols

reg = ols('quantity ~ kind', data = data).fit()
table = sm.stats.anova_lm(reg, typ=1) # anova 테스트 typ = 2 를 보통 많이씀
print(table) # 분산 분석표 출력 # F 값은 = 27.980888 / 228.922922 ( method의 mean_sq / Residual의 mean_sq )
# 해석 : 0.428149 > 0.05 귀무 채택, 기름의 종류에 따라 흡수율에 차이가 없다

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# post hoc test (사후 검정)

tukeyResult = pairwise_tukeyhsd(endog=data['quantity'], groups=data['kind'], alpha = 0.05)
print(tukeyResult)

#===============================================================================

# =====================================================
# group1 group2 meandiff p-adj   lower    upper  reject
# -----------------------------------------------------
#      1      2   5.5789   0.94  -22.494 33.6519  False
#      1      3   3.4956 0.9884 -27.8909 34.8822  False
#      1      4   9.4956 0.8223 -21.8909 40.8822  False
#      2      3  -2.0833 0.9975 -33.4699 29.3032  False
#      2      4   3.9167 0.9838 -27.4699 35.3032  False
#      3      4      6.0 0.9581 -28.3822 40.3822  False
# -----------------------------------------------------

#===============================================================================




# [ANOVA 예제 2]
#
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
#
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

import MySQLdb
import pickle
import pandas as pd

with open('mydb.dat',mode='rb') as obj:
    config =pickle.load(obj)

try:
    conn= MySQLdb.connect(**config)
    cursor=conn.cursor()
    
    sql='''select buser_name, jikwon_pay
            from jikwon join buser on buser_no = buser_num'''
    
    cursor.execute(sql)
    df=cursor.fetchall()
    df = pd.read_sql(sql,conn)
    
    df.columns=['부서','연봉']
    print(df)
    data1 = df[df.iloc[:,0]=='총무부'].iloc[:,1] # 총무부 연봉
    data2 = df[df.iloc[:,0]=='영업부'].iloc[:,1] # 영업부 연봉
    data3 = df[df.iloc[:,0]=='전산부'].iloc[:,1] # 전산부 연봉
    data4 = df[df.iloc[:,0]=='관리부'].iloc[:,1] # 관리부 연봉
    
    # 정규성 검정
    print(stats.shapiro(data1).pvalue) # 0.026  # 불만족
    print(stats.shapiro(data2).pvalue) # 0.025  # 불만족
    print(stats.shapiro(data3).pvalue) # 0.419  # 만족
    print(stats.shapiro(data4).pvalue) # 0.907  # 만족  
    
    print(stats.ks_2samp(data1, data2).pvalue)  # 0.335 # 아래도 모두 만족
    print(stats.ks_2samp(data1, data3).pvalue)
    print(stats.ks_2samp(data1, data4).pvalue)
    print(stats.ks_2samp(data2, data3).pvalue)
    print(stats.ks_2samp(data2, data4).pvalue)
    print(stats.ks_2samp(data3, data4).pvalue)
    
    # 등분산성 검정
    print(stats.levene(d1,d2,d3,d4).pvalue) # 0.326 만족
    
    print()
    
    # 검정
    reg = ols('연봉 ~ 부서', data = df).fit()
    table = sm.stats.anova_lm(reg, typ=1) # anova 테스트 typ = 2 를 보통 많이씀
    print(table) # 분산 분석표 출력
    # 해석 : pvalue 0.745442 > 0.05 귀무 채택, 부서별 직원의 연봉엔 차이가 없다
    
    # 사후 검정
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    # post hoc test (사후 검정)
    
    tukeyResult = pairwise_tukeyhsd(endog=df['연봉'], groups=df['부서'], alpha = 0.05)
    print(tukeyResult)
    
    #===========================================================================
    # ===========================================================
    # group1 group2  meandiff  p-adj    lower      upper   reject
    # -----------------------------------------------------------
    #    관리부    영업부 -1354.1667 0.6937 -4736.5568 2028.2234  False
    #    관리부    전산부  -933.9286  0.897 -4605.9199 2738.0628  False
    #    관리부    총무부  -848.2143 0.9202 -4520.2056 2823.7771  False
    #    영업부    전산부   420.2381 0.9756 -2366.0209 3206.4971  False
    #    영업부    총무부   505.9524 0.9588 -2280.3066 3292.2114  False
    #    전산부    총무부    85.7143 0.9998 -3045.7705  3217.199  False
    # -----------------------------------------------------------
    #===========================================================================
    
except Exception as e:
    print('에러: '+e)

finally:
    cursor.close()
    conn.close()