# 차트의 종류 경험하기 : data의 성격에 따라 차트를 적용하는 것이 중요함

import numpy as np
import matplotlib.pyplot as plt

# 차트 영역 객체 선언시 matplotlib 스타일 관련 인터페이스 유형
'''
x = np.arange(10)

# 방법 1 : matplotlib 스타일
plt.figure() # plot 그림을 생성
plt.subplot(2,1,1) # ( row, column, panel number(active) )
plt.plot(x,np.sin(x))
plt.subplot(2,1,2) # ( row, column, panel number(active) )
plt.plot(x,np.cos(x))
plt.show()

# 방법 2 : 객체지향 인터페이스
fig, ax = plt.subplots(nrows=2,ncols=1)
ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))
plt.show()
'''
# fig = plt.figure() # 명시적으로 차트영역객체 선언
# ax1 = fig.add_subplot(1,2,1) # 1행 2열
# ax2 = fig.add_subplot(1,2,2)
#
# ax1.hist(np.random.randn(10), bins=5, alpha = 0.9)
# ax2.plot(np.random.randn(10))
# plt.show()

# data = [50,80,100,70,90]
# plt.bar(range(len(data)),data) # 가로막대
# plt.show()
#
# data = [50,80,100,70,90]
# err = np.random.rand(len(data))
# plt.barh(range(len(data)),data, xerr=err) # 세로막대 # xerr 에러막대 표시
# plt.show()

# data = [50,80,100,70,90]
# plt.pie(data, explode=(0,0.4,0.1,0,0),colors=['yellow', 'blue','red']) # explode - pie형에서 해당 데이터를 분리할 때 씀
# plt.show()
#
# plt.boxplot(data) # 최대값, 최소값, 중앙값 등이 표현
# plt.show()

import seaborn as sns # matplotlib의 기능을 추가
import pandas as pd
titanic = sns.load_dataset('titanic') # seaborn 에서 기본적으로 제공하는 dataset이 있음
pd.set_option('display.max_columns',500)
print(titanic.head(3))
print(titanic.info())

sns.distplot(titanic['age'])
#plt.show()

sns.boxenplot(y='age',data=titanic)
#plt.show()

ti_pivot = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
#print(ti_pivot)

sns.heatmap(ti_pivot)
plt.show()