# 회귀분석 문제 5) 
# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# testdata 폴더 : Consumo_cerveja.csv
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#             Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오
# 조건 : NaN이 있는 경우 삭제!

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler # 정규화 지원
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


df = pd.read_csv('../testdata/Consumo_cerveja.csv', usecols = [1,4,6])
df['Temperatura Media (C)'] = df['Temperatura Media (C)'].str.replace(',', '.').apply(float)
df['Precipitacao (mm)'] = df['Precipitacao (mm)'].str.replace(',', '.').apply(float)
df = df.dropna(axis=0)
print(df.info())
print(df.head(3))

x = df[['Temperatura Media (C)', 'Precipitacao (mm)']]
y = df[['Consumo de cerveja (litros)']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)
print(model.intercept_, model.coef_)
y_pred = model.predict(x_test)
# print('예측값 :', y_pred)
# print('실제값 :', y_test.values)

print('결정계수로 모델 성능을 확인')
print('결정계수 :', r2_score(y_test, y_pred)) # test data를 사용
print('mean_squared_error(RMSE, 평균제곱오차):{}'.format(mean_squared_error(y_test, y_pred)))
print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_test, y_pred)))

 # 독립변수 값이기 때문에 metrix로 넣어주어야 된다.


new_pred = model.predict([[24.82, 0.0]])
print('예측 맥주 소비량은 %s입니다.'%new_pred[0][0])