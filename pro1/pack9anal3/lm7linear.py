# 선형회귀분석모델 작성 시 LinearRegression을 사용 - summary() 함수 지원안한다
# 분석모델을 평가할 수 있는 score알아보기

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error # << mean_squared_error 알아둬야함
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 편차가 있는 표본 데이터 작성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0,10,sample_size)
y = np.random.normal(0,10,sample_size) + x *30
print(x[:5])
print(y[:5])
print('상관계수 :',np.corrcoef(x,y)) # 0.99939357

# 독립변수 x에 대한 정규화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1,1)) # 2차원 배열로 reshape을 하면 어떻겠니~~ 라고 권유 중 Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
print(x_scaled) # 왜 2차원 배열로 만들었나~~~하면 sklearn 에서는 matrix만 입력할 수 있도록 요구하기 때문이다

# # 시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled,y)
y_pred = model.predict(x_scaled)

print('예측값 :', y_pred[:10])
print('실제값 :', y[:10])

print()
# 모델 성능 파악용 함수 작성
def RegScore_func(y_true, y_pred):
    print('r2_score(결정계수) :{}'.format(r2_score(y_true, y_pred)))
    print('explained_variance_score(설명된 분산 점수) :{}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(RMSE,평균제곱오차 :{}'.format(mean_squared_error(y_true, y_pred)))
    # 평균제곱오차 : 예측값에서 실제값(관찰값)을 뺀 값의 제곱의 합을 표본수로 나눈 것
    
RegScore_func(y,y_pred)