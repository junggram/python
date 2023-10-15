# KNN

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

cancer = load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, 
                                                    stratify=cancer.target, random_state=66)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (426, 30) (143, 30) (426,) (143,)

train_acc = []
test_acc = []

neighbors_setting = range(1, 11) # 10개

for n_neigh in neighbors_setting:
    clf = KNeighborsClassifier(n_neighbors=n_neigh)
    clf.fit(x_train, y_train)
    train_acc.append(clf.score(x_train, y_train))
    test_acc.append(clf.score(x_test, y_test))


import numpy as np
print('train 분류 평균 정확도 : ', np.mean(train_acc))  # 둘의 차이가 크면 오버피팅
print('test 분류 평균 정확도 : ', np.mean(test_acc))

plt.plot(neighbors_setting, train_acc, label='train acc') # x:neighbors_setting , y:train_acc
plt.plot(neighbors_setting, test_acc, label='test acc')
plt.ylabel('accuracy')
plt.xlabel('k값')
plt.legend()
plt.show()

