# Ensemble Learning : 개별적인 여러 모델들을 모아 종합적으로 취합 후 최종 분류 결과를 출력
# 종류로는 voting, bagging, boosting 방법이 있다.
# breast_cancer dataset을 사용
# LogisticRegression, Decision Tree, KNN을 사용하여 voting 분류기 작성
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()
data_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
print(data_df.head(2))

# train / test split
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=1, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (455, 30) (114, 30) (455,) (114,)
print(x_train[:3])
print(y_train[:3],set(y_train)) # {0, 1} : 0이 양성, 1이 음성

# Ensemble model (VotingClassifier) : LogisticRegression + KNN + DecisionTreeClassifier
logi_regression = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors=3)
dmodel = DecisionTreeClassifier()

voting_model = VotingClassifier(estimators=[('LR',logi_regression),
                                             ('KNN',knn),
                                              ('Decision',dmodel)],
                                            voting='soft') # 보팅모델 인자로 튜플타입
                                                           # hard = 단순히 결과값을 계산해서 다수결의 원칙
                                                           # soft = 확률값 계산해서 높은확률
classifiers = [logi_regression, knn, dmodel]

# 개별 모델의 학습 및 평가
for classifier in classifiers :
    classifier.fit(x_train, y_train)
    pred = classifier.predict(x_test)
    class_name = classifier.__class__.__name__
    print('{0}정확도 : {1:.4f}'.format(class_name, accuracy_score(y_test, pred)))
    
# 앙상블 모델 학습 및 평가
voting_model.fit(x_train, y_train)
Vpred = voting_model.predict(x_test)
print('앙상블 모델의 정확도 : {0:.4f}'.format(accuracy_score(y_test,Vpred)))