# 다항분류 (얘는 활성화 함수 softmax - 결과값을 확률로 반환) 
# softmax 함수를 사용하기 때문
# iris dataset을 사용 - 꽃의 종류를 3가지로 분류할 때마다

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics._scorer import accuracy_scorer
from sklearn.preprocessing import StandardScaler # 표준화 , MinMaxScaler : 정규화
from sklearn import datasets
from sklearn.metrics._classification import accuracy_score


iris = datasets.load_iris()
# print(iris.DESCR)
print(iris.keys())

x = iris.data
# print(x)
print(np.corrcoef(x[:,2],x[:,3])) # 0.96286543

x = iris.data[:,[2,3]] # petal.length, petal.width
y = iris.target
print(x[:3])
print(y[:3], ' ',set(y)) # {0, 1, 2} target의 종류가 세가지

# train / test split (7:3)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (105, 2) (45, 2) (105,) (45,)

""" 
# data scaling : 표준화 - 최적화 과정에서 안정성 수렴 속도 향상, 오버/언더 플로우 방지 가능
print(x_train[:3])
'''[[3.5 1. ]
 [5.5 1.8]
 [5.7 2.5]]'''

sc = StandardScaler()
sc.fit(x_train); sc.fit(x_test) # 표준화는 연속형인 독립변수만, 범주형인 종속변수는 하지 않는다

x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])
'''[[-0.05624622 -0.18650096]
 [ 1.14902997  0.93250481]
 [ 1.26955759  1.91163486]]'''
 
# 스케일링 자료 원상복구
inver_x_train = sc.inverse_transform(x_train)
inver_x_test = sc.inverse_transform(x_test)
"""
from sklearn.tree import DecisionTreeClassifier
# model = LogisticRegression(C=1.0, random_state = 0, verbose=0) # C=1.0 L2 규제(패널티 적용) - 값이 작을수록 규제는 강화됨, 오버피팅 발생 시에 숫자를 줄여봐라
                                  # 모델을 튜닝할 때 C 를 조절 (오버/언더 피팅 조절)
                                  # verbose 는 학습과정을 보여준다 기본값은 0
                                  
model = DecisionTreeClassifier(criterion = 'entropy', max_depth=5)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print('예상치 :',y_pred)
print('실제값 :',y_test)
print('총갯수 :%d, 오류수:%d'%(len(y_test), (y_test != y_pred).sum()))
# 분류 정확도 1
print('분류 정확도 :',accuracy_score(y_test, y_pred))

# 분류 정확도 2
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측치'], colnames=['관측치'])
print(con_mat)
print((con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))

# 분류 정확도 3
print('test :',model.score(x_test,y_test))
print('train :',model.score(x_train,y_train)) # test와 차이가 크지 않기 때문에 과적합이 아니다~~

# 모델 저장
import joblib
joblib.dump(model,'iris.csv')

mymodel = joblib.load('iris.csv')

# 새로운 값으로 분류 예측
print(x_test[:1])
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [3.4, 0.2]])
# 참고 : 만약 표준화로 학습했다면 new_data도 표준화 해줘야 한다.
new_pred = mymodel.predict(new_data) # # softmax가 반환한 결과 중 가장 큰 인덱스를 취한 결과
print('예측 결과 :',new_pred)
print(mymodel.predict_proba(new_data)) # softmax가 반환한 결과
"""
[[9.96150873e-05 8.40157413e-02 9.15884644e-01]    2 제일큼
 [9.98114817e-01 1.88518127e-03 1.94610093e-09]    0 꼴등임
 [1.75251457e-01 8.23787901e-01 9.60641983e-04]]   1 다음큼
"""

# 시각화
from matplotlib.colors import ListedColormap

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')        # 점 표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 인자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)       # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프 상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=mymodel, test_idx=range(105, 150), title='scikit-learn제공')


# Graphviz 모듈로 시각화
from sklearn import tree
from io import StringIO
import pydotplus

dot_data = StringIO() # 파일 흉내를 내는 역할
tree.export_graphviz(mymodel, out_file = dot_data, feature_names = iris.feature_names[2:4])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree2.png')

# 이미지 읽기
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
img = imread('tree2.png')
plt.imshow(img)
plt.show()
