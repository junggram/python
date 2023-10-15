# DecisionTreeRegressor, RandomForestRegressor 으로 정량적인 예측 모델

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor # classifier 말고 regressor
from sklearn.ensemble import RandomForestRegressor # classifier 말고 regressor
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score
boston = load_boston()
# print(boston.keys())

dfx = pd.DataFrame(boston.data, columns = boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=['MEDV'])
df = pd.concat([dfx, dfy], axis=1)

print(df.head(5))
print(df.corr())

# 시각화

cols = ['MEDV','RM','LSTAT']
# sns.pairplot(df[cols])
# plt.show()  # MEDV : RM = 양의 상관관계,  MEDV : LSTAT = 음의 상관관계

# 단순 선형회귀
x = df[['LSTAT']].values
y = df['MEDV'].values

print(x[:3])
print(y[:3])

print('DecisionTreeRegressor---------------------')
model = DecisionTreeRegressor(criterion='mse').fit(x,y)
print('예측값 :',model.predict(x)[:5])
print('실제값 :',y[:5])
print('결정계수 :',r2_score(y, model.predict(x))) # 결정계수 : 0.959

print('RandomForestRegressor---------------------')
model2 = RandomForestRegressor(criterion='mse', n_estimators=100, random_state=123).fit(x,y)
print('예측값 :',model2.predict(x)[:5])
print('실제값 :',y[:5])
print('결정계수 :',r2_score(y, model2.predict(x))) # 결정계수 : 0.908