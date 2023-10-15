# 카이제곱 검정 중 일원카이제곱
# : 관찰도수가 기대도수와 일치하는 지를 검정하는 방법
# : 종류 : 적합도/선호도 검정
# - 범주형 변수가 한 가지로, 관찰도수가 기대도수에 일치하는지 검정한다.

# 적합도 검정
# : 자연현상이나 각종 실험을 통해 관찰되는 도수들이 귀무가설 하의 분포(범주형 자료의 각 수준별 비율)에 얼마나 일치하는가에 대한
# 분석을 적합도 검정이라 한다.
# : 관측값들이 어떤 이론적 분포를 따르고 있는지를 검정으로 한 개의 요인을 대상으로 함.
#
# <적합도 검정실습>
# 주사위를 60 회 던져서 나온 관측도수 / 기대도수가 아래와 같이 나온 경우에 이 주사위는 적합한 주사위가 맞는가를 일원카이제곱 검정
# 으로 분석하자.
#
# 주사위 눈금 1   2    3    4    5   6
# 관측도수    4   6   17   16   8   9
# 기대도수   10  10   10   10   10  10

# 귀무 가설 : 기대치와 관찰치는 차이가 있다. 현재 주사위는 게임에 적합하다 (대체로 보수적)
# 대립 가설 : 기대치와 관찰치는 차이가 있다. 현재 주사위는 게임에 적합하지 않다
# 일원카이제곱 stats.chisquare(관찰 빈도, 예상 빈도) 편도 카이제곱

import pandas as pd
import scipy.stats as stats

data = [4,6,17,16,8,9]
result = stats.chisquare(f_obs=data)
print(result)
print('chi2:{}, p-value:{}'.format(result.statistic, result.pvalue))
print('statistic:%.5f,p-value:%5f'%(result)) # 소수점 5번째까지 표시~  # statistic:14.20000,p-value:0.014388
# 판정 : p-value:0.01439 <0.05 이므로 귀무 기각
# 기대치와 관찰치는 차이가 있다. 현재 주사위는 게임에 적합하지 않다. 현재관찰된 데이터는 우연히 발생한 데이터가 아니다
# cv로 판정 df(자유도): 5   cv: 11.07     statistic:14.2  = 귀무기각역에 존재 = 귀무기각

data = [11,6,10,13,8,12]
result = stats.chisquare(f_obs=data)
print(result)
print('chi2:{}, p-value:{}'.format(result.statistic, result.pvalue))
print('statistic:%.5f,p-value:%5f'%(result)) # 소수점 5번째까지 표시~
# 판정 : p-value:0.638570 > 0.05 이므로 귀무 채택
# 현재 주사위는 게임에 적합하다


print('------선호도---------------------')
# <선호도 분석 실습> 5개의 스포츠 음료에 대한 선호도에 차이가 있는지 검정
# 귀무 : 스포츠음료에 대한 선호도에 차이가 없다
# 대립 : 스포츠음료에 대한 선호도에 차이가 있다
datas = pd.read_csv('../testdata/drinkdata.csv')
print(datas)
print(sum(datas.관측도수))
print(stats.chisquare(datas.관측도수))
# statistic=20.488188976377952  pvalue=0.00039991784008227264 < 0.05 이므로 # 귀무 기각
# 스포츠 음료에 대한 선호도에 차이가 있다. 그러므로 특정음료 제공을 더 많이 할 수 있도록 한다.

