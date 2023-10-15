# 단순 선형 회귀모델
# 기본적인 결정론적 선형회귀 방법 : 독립변수에 대해 대응하는 종속변수와 유사한 예측값을 출력하는 함수 f(x)를 찾는 작업이다
import pandas as pd

df = pd.read_csv('../testdata/drinking_water.csv')
print(df.head(3))
print(df.corr())
print(df.info())

import statsmodels.formula.api as smf

# 적절성이 만족도에 영향을 준다 라는 가정하에 모델을 생성
model = smf.ols(formula = '만족도 ~ 적절성',data=df).fit() # formula = 종속변수 ~ 독립변수

print(model.summary()) # 생성된 모델의 요약결과를 반환. 능력치를 확인   
# Prob (F-statistic) = p-value : 2.24e-52 < 0.05
# 독립변수는 종속변수에 통계적으로 유의하다

# t-value : 19.340  =  coef(0.7393) 를 std err(0.038) 로 나눈값  =  0.7393 / 0.038
# F-statistic : 374.0  =  t-value를 제곱한 값
# F-statistic, t-value 커지면 p-value값이 작아진다 (모델의 성능이 좋아진다 => 모델의 설명력은 (R-squared) 로 나타낸다)
# std(표준편차), std err(표준오차)가 작을수록 데이터들이 예측선에 가까이 있다, 잔차가 작다, 데이터가 밀집되어있다
# R-squared(결정계수) : 0.588  =  독립변수가 종속변수의 분산을 설명하는 비율 , 0 ~ 1, 표준오차가 작아질수록 R-squared는 커진다 (설명력이 좋아진다, 모델의 성능이 좋다)

# Durbin-Watson :  2.185  =  잔차의 독립성 확인, 2와 가까울수록 좋다

# Jarque-Bera (JB): 16.003    # Prob(JB)와 함께 적합도 판단
# Prob(JB): 0.000335 

# Skew : -0.328    # 왜도, 0에 가까울수록 정규분포를 따름, 양수이면 오른쪽으로 치우침
# Kurtosis : 4.012    # 첨도, 양수면 뾰족함, 1보다 작으면 완만함

print(0.7393/0.038,'= t-value') # 19.45 t값과
print((0.7393/0.038)**2,'= F-statistic') # 378.50 f-statistic값이 조금씩 차이가 있을 수 있는데


#===============================================================================
# 
#===============================================================================

print('회귀계수 :',model.params)
print('결정계수 :',model.rsquared)
print('유의확률 :',model.pvalues)
print('예측값 :',model.predict()[:5])
print('실제값 :',df['만족도'][:5].values)

print()
new_df = pd.DataFrame({'적절성':[4,3,2,1]})
new_pred = model.predict(new_df)
print('예측결과 :',new_pred)