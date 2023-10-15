# 특성공학 기법 중 차원축소(PCA - 주성분 분석) 
# n개의 관측치와 p개의 변수로 구성된 데이터를 상관관계가 최소화 된 k개의 변수로 축소된 데이터를 만든다.
# 데이터의 분산을 최대한 보존하는 새로운 축을 찾고 그 축에 데이터를 사영시키는 기법. 직교
# 목적 : 독립변수(x, feature)의 갯수를 줄임. 이미지 차원 축소로 용량을 최소화 함

# iris dataset으로 PCA를 진행

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
n = 10
x = iris.data[:n, :2]
print(x, x.shape)
print(x.T)

# plt.plot(x.T, 'o:')
# plt.xticks(range(2))
# plt.grid()
# plt.legend(['표본{}'.format(i) for i in range(n)])
# plt.show()

# 산점도 (산포도)
# df = pd.DataFrame(x)
# # print(df.head(3))
# ax = sns.scatterplot(0,1, data = pd.DataFrame(x), marker='s', s=100, color='blue')
# for i in range(n):
#     ax.text(x[i,0] - 0.05, x[i,1]-0.07, '표본{}'.format(i+1)) # 가시성을 위해 절편값을 조절 
#
# plt.xlabel('꽃받침길이')
# plt.ylabel('꽃받침너비')
# plt.axis('equal')
# plt.show()

# PCA  (비지도학습)
pca1 = PCA(n_components=1) # 변환할 차원 수(?) 
x_low = pca1.fit_transform(x) # x값을 차원축소 한다는 말 : 2차원 -> 1차원 (차원 축소된 근사 데이터), 비지도학습
print('x_low :', x_low, ' ',x_low.shape)

x2 = pca1. inverse_transform(x_low) # 차원 축소된 근사 데이터를 원상복구 (
print('원복된 결과 :', x2, ' ', x2.shape)

print(x)
print(x_low[0])
print(x2[0,:])
print(x[0])

# 시각화
# ax = sns.scatterplot(0,1, data = pd.DataFrame(x), marker='s', s=100, color='blue')
# for i in range(n):
#     d = 0.03 if x[i,1] > x2[i,1] else -0.04
#     ax.text(x[i,0] - 0.05, x[i,1] - d, '표본{}'.format(i+1)) # 가시성을 위해 절편값을 조절 
#     plt.plot([x[i,0], x2[i,0]], [x[i,1], x2[i,1]],'k--' ) # 분산끼리 선으로 연결
#
# plt.plot(x2[:,0], x2[:,1], 'o-', color='red', markersize=10, marker='o') # 분산값이 가장 큰 직교하는 선을 그려봄
# plt.xlabel('꽃받침길이')
# plt.ylabel('꽃받침너비')
# plt.axis('equal')
# plt.show()

# iris 4개의 열을 모두 참여 시켜서 차원축소를 해보자 (4개 -> 2개로)

x = iris.data
pca2 = PCA(n_components=2) # 2개의 열로 줄인다
x_low2 = pca2.fit_transform(x)
print('x_low2 :',x_low2, ' ', x_low2.shape) # 어떻게 합쳐진지는 모르지만 일단 축소됨 (짐작이 가능하긴 함)
#===============================================================================
print(pca2.explained_variance_ratio_) # 설명서 (변동성 비율 ******중요함 꼭봐야함******)
# 전체 변동성에서 개별 PCA결과(개별 component) 별로 차지하는 변동성 비율
# [0.92461872 0.05306648] 
# 0.9776852 : 첫번째 컴포넌트가 전체데이터의 92.4%설명, 두번째 컴포넌트가 5%설명 합쳐서
            # 두개의 컴포넌트가 전체 원본 데이터의 97.7% 설명함
#===============================================================================

x4 = pca2.inverse_transform(x_low2)
print('최초 자료 :',x[0])
print('차원 축소 :',x_low2[0]) # 근사치로 출력
print('차원 복구 :',x4[0]) # 근사치로 출력, PCA를 통해 근사행렬로 변환됨

print()
iris2 = pd.DataFrame(x_low2, columns=['f1','f2']) # 칼럼의 분류가 어떻게 되어있는지 모르기 때문에 임의로 명명함
print(iris2.head(3))

