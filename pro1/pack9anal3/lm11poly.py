# 선형회귀모델을 다항회귀모델로 변환
# 선형 가정이 신뢰도가 떨어질 경우 대처 방법으로 다항식을 추가할 수 있다.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20])
y = np.array([15,13,12,11,10,9,8,7,6,5,8,9,10,11,15,17,18,19,22])



print(np.corrcoef(x,y))

# plt.scatter(x,y)
# plt.show()

# 선형회귀모델 작성

from sklearn.linear_model import LinearRegression

x = x[:, np.newaxis] # 차원 확대 
# print(x)
model = LinearRegression().fit(x,y)
ypred = model.predict(x)
print(ypred)

# plt.scatter(x,y)
# plt.plot(x, ypred, c='red')
# plt.show()

# 좀 더 복잡한 형태의 모델을 필요 : 다항식 특징을 추가하(feature)을 추가한 다항회귀모델 작성
from sklearn.preprocessing import PolynomialFeatures # 다항식특징

poly = PolynomialFeatures(degree=2, include_bias=False) # degree : 열의 갯수 / include_bias=False : 절편은 상관없다
x2 = poly.fit_transform(x)
print(x2)

model2 = LinearRegression().fit(x2,y) # 특징 행렬값으로 학습
ypred2 = model2.predict(x2)
print(ypred)

plt.scatter(x,y)
plt.plot(x, ypred2, c='red') # y값만 바꾼다, 선형회귀 모델을 비선형회귀 모델로 바꿔주는것 뿐 - 직선에서 곡선형태로
plt.show()