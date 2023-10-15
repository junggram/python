# ROC (Receiver Operating Characteristic) curve
# ROC 커브는 모든 가능한 threshold에 대해 분류모델의 성능을 평가하는데 사용된다
# ROC 커브 아래의 영역을 AUC (Area Under thet Curve)라 합니다

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
x,y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=123) # n_redundant=0 선형조합을 표시하는 성분의 갯수
print(x[:3])
print(y[:3])

# import matplotlib.pyplot as plt
# plt.scatter(x[:,0],x[:,1])
# plt.show()

model = LogisticRegression().fit(x,y)
y_hat = model.predict(x)
print('예측값 :',y_hat[:3])

print()
f_value = model.decision_function(x) # 판별 함수 (결정 함수) : 판별 경계선 설정을 위해서 샘플을 얻기
# print('f_value :',f_value)

df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f','y_hat','y'])
print(df)

print()
print(confusion_matrix(y, y_hat)) # [[44  4]
                                   # [ 8 44]]
                                   
acc = (44+44) / 100         # (TP + TN) / 전체수   # 정확도
recall = 44 / (44 + 4)      # TP / (TP + FN)     # 재현률
precision = 44 / (44 + 8)   # TP / (TP + FP)     # 정밀도
specificity = 44 / (8 + 44) # TN / (FP + TN)     # 특이도
fallout = 8 / (8 + 44)      # FP / (FP + TN)     # 위양성률

print('acc(정확도) :',acc)
print('recall(재현률) :',recall)       # TPR
print('precision(정밀도) :',precision)
print('specificity(특이도) :',specificity)
print('fallout(위양성률) :',fallout)   # FPR
print('fallout(위양성률) :',1 - specificity)

print() # 정확도 구하는 다른 방법
from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('accuracy_score(정확도) :',ac_sco)

cl_rep = metrics.classification_report(y,y_hat)
print('classification_report :',cl_rep) # acc, precision, recall, f1-score 가 나와있음

print()
fpr, tpr, threshold = metrics.roc_curve(y,model.decision_function(x))
print('fpr :',fpr)
print('tpr :',tpr)
print('threshold (분류결정 임계값) :',threshold) # positive 예측값을 결정하는 확률 기준값

# ROC 커브
import matplotlib.pyplot as plt
plt.plot(fpr,tpr,'o-',label = 'Logistic Regression')
plt.plot([0,1],[0,1],'k--',label='random classifier line(AUC:0.5)')
plt.plot([fallout],[recall],'ro',ms=10)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend() # plt.label 이 보이려면 적어줘야함
plt.show()

# AUC : ROC 커브의 면적
print('AUC :',metrics.auc(fpr,tpr)) # 1에 근사할수록 좋은 분류모델
