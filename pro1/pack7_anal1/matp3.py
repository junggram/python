# yahoo 제공 주식 정보 읽기
# pip install pandas_datareader

import pandas as pd
from pandas_datareader import data

# pickle로 저장된 코스닥 / 코스피 종목 코드 읽기
kosdaq = pd.read_pickle('kosdaq.pickle')
kospi = pd.read_pickle('kospi.pickle')
# print(kosdaq.head(5)) # 제일홀딩스 003380
# print(kospi.head(5)) #넷마블게임즈 251270

print()
start_date = '2018-01-01'
tickers = ['003380.KQ', '251270.KS']
holding_df = data.get_data_yahoo(tickers[0], start_date)
net_df = data.get_data_yahoo(tickers[1], start_date)
print(holding_df)
print()
print(net_df)

holding_df.to_pickle('홀딩스.pickle')
net_df.to_csv('넷마블.csv')

# 시각화
import matplotlib.pyplot as plt
plt.plot(net_df)
plt.show()

import seaborn as sns
sns.scatterplot(x='Open',y='Close',data=net_df)
plt.show()

