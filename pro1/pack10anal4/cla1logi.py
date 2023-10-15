# 로지스틱 회귀분석 (Logistic Regression)
# 종속변수와 독립변수 간의 관계로 예측모델을 생성한다는 점에서 선형회귀분석과 유사하다.
# 하지만 독립변수(x)에 의해 종속변수(y)의 범주로 분류한다는 측면에서 분류분석 방법이다.
# 분류 문제에서 선형 예측에 시그모이드 함수를 적용하여 가능한 각 불연속 라벨 값에 대한 확률을 생성하는 모델로
# 이진분류 문제에 흔히 사용되지만 다중클래스 분류(다중 클래스 로지스틱 회귀 또는 다항 회귀 )에도 사용될 수 있다.
# 독립변수 : 연속형, 종속변수 : 범주형
# 뉴럴네트워크(신경망)에서 사용됨

import math

def sigFunc(x):
    return 1 / (1 + math.exp(-x)) # 시그모이드 함수 처리

print(sigFunc(3)) # 인자값은 로짓 전환된 값이라 가정
print(sigFunc(1))
print(sigFunc(37.6))
print(sigFunc(-3.4))

print('mtcars dataset으로 분류 모델 작성')
import statsmodels.api as sm

carData = sm.datasets.get_rdataset('mtcars')
print(carData.keys())
carDatas = sm.datasets.get_rdataset('mtcars').data
print(carDatas)
mtcar = carDatas.loc[:,['mpg','hp','am']]
print(mtcar.head(3))
print(mtcar['am'].unique()) # [1 0] 이항분류
print(mtcar.shape) # [32 3]

# 연비와 마력수에 따른 변속기 분류(수동, 자동)
# 모델 작성 1 : logit()
import statsmodels.formula.api as smf
import numpy as np
formula = 'am ~ hp + mpg'
result = smf.logit(formula = formula, data = mtcar).fit()
print(result)
print(result.summary())
# print('예측값 :',result.predict())

pred = result.predict(mtcar[:10])
print('예측값 :',pred.values)
print('예측값 :',np.around(pred.values)) # 0.5를 기준으로 0과 1로 출력한다 (반올림)
print('실제값 :',mtcar['am'][:10].values)

print()
conf_tab = result.pred_table() # confusion matrix (혼돈 행렬)
print(conf_tab)
print('분류 정확도 :',(16+10) / len(mtcar))
print('분류 정확도 :',(conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))

from sklearn.metrics import accuracy_score

pred2 = result.predict(mtcar)
print('분류 정확도 :',accuracy_score(mtcar['am'], np.around(pred2))) # 선형회귀모델에선 00%의 설명력을 가지고있다~~ 라고 확정을 하지 않고 애매~~~하게 했는데
                                                                   # 분류에서는 정확도 accuracy라고 확정을 지었다

print('-------------------------------')
# 모델 작성 2 : glm() - 일반화된 선형모델
result2 = smf.glm(formula = formula, data = mtcar, family = sm.families.Binomial()).fit() # family의 기본값은 가우시안 이다.
                                                                                        # 이항분포를 위해 Binomial 을 사용
                                                                                  
print(result2)
print(result2.summary())
print()

glm_pred = result2.predict(mtcar[:10])
print('예측값 :',np.around(glm_pred.values))
print('실제값 :',mtcar['am'][:10].values)

glm_pred2 = result2.predict(mtcar)
print('glm 분류 정확도 :', accuracy_score(mtcar['am'],np.around(glm_pred2)))

print('\n새로운 값으로 분류 예측')
newdf = mtcar.iloc[:2].copy()
print(newdf)
newdf['mpg'] = [50,20]
newdf['hp'] = [100,110]
print(newdf)

new_pred = result2.predict(newdf)
print('분류 예측결과:',np.around(new_pred.values))
