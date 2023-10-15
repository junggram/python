import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('서울시_우리마을가게_상권분석서비스(구_상권배후지_생활인구)_2021년.csv', encoding='euc-kr')
# print(data.head(2))
del data['기준_년_코드']
del data['기준_분기_코드']
print(data.corr())
# print(data.isnull().sum())

corr = data.corr()
print(corr.isnull().sum())
# 시각화
sns.pairplot(data, diag_kind='kde')
plt.show()

corr.to_csv('상관관계2.csv')
