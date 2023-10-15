# 날씨정보 데이터로 이항분류 : 내일 비가 오니 안오니?

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

data = pd.read_csv('../testdata/weather.csv')
print(data.head(3),data.shape)  # (366, 12)

data = data.drop(['Date','RainToday'], axis=1)
print(data.head(3),data.shape)  # (366, 10)
data['RainTomorrow'] = data['RainTomorrow'].map({'Yes':1, 'No':0}) # Dummy
print(data.head(2))
print(data['RainTomorrow'].unique())    # [1 0]
#RainTomorrow : 종속변수, 그 외는 독립변수

# train / test split == 7 : 3  ( 7:3 비율로 나누기 )
train, test = train_test_split(data, test_size=0.3, random_state=42)    # R에서는 없지만 파이썬에서는 있다
print(train.shape, test.shape)   # (256, 10) (110, 10)

col_select = '+'.join(train.columns.difference(['RainTomorrow'])) # 칼럼을 하나하나 다 쓰기 힘드니 'RainTomorrow' 제외한 나머지칼럼만 선택하는 코드로 편하게~~
my_formula = 'RainTomorrow ~ ' + col_select
print(my_formula)
model = smf.glm(formula = my_formula, data = train, family = sm.families.Binomial()).fit()
print(model.summary())  # p-value가 0.05 보다 심하게 큰 것들은 빼야하지만 일단 그냥 진행한다
# print(model.params)

print('예측값 :',np.around(model.predict(test).values))
print('예측값 :',np.rint(model.predict(test).values))

print('실제값 :',test['RainTomorrow'].values)

# 정확도
# conf_matrix = model.pred_table()
# print('conf_matrix :\n', conf_matrix)   # 에러    # AttributeError: 'GLMResults' object has no attribute 'pred_table'
#                                         # logit으로 바꿔야함

model = smf.logit(formula = my_formula, data = train, family = sm.families.Binomial()).fit()
        # glm을 logit으로 바꿔서 하자

conf_matrix = model.pred_table()
print('conf_matrix :\n', conf_matrix)
print('분류 정확도 :', (conf_matrix[0][0] + conf_matrix[1][1]) / len(train))

from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('분류 정확도 :', accuracy_score(test['RainTomorrow'], np.around(pred)))

# 머신러닝의 포용성(inclusion, tolerance)
# 통계 및 추론 모델로 새로운 값을 예측
# y = w * 2 + 0  수학에서는 100%의 답을 원함
# 통계에서는 4의 주변값이 나올 수 있도록 학습을 함
# 예를 들어 개 이미지 분류를 하는 경우 꼬리가 없는 개도 정확하게 분류되도록 하는 것이 머신러닝의 목적
# 포용성이 있는 모델이라 함은 데이터 분류 인식률이 80%, 90%가 되는 것이 100%인 경우보다 더 효과적이다


