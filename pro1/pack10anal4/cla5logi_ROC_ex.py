# [로지스틱 분류분석 문제3] 
#
# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용

#   참여 칼럼 :
#   Daily Time Spent on Site : 사이트 이용 시간 (분)
#   Age : 나이,
#   Area Income : 지역 소독,
#   Daily Internet Usage:일별 인터넷 사용량(분),
#   Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )

# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# ROC 커브와 AUC 출력

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import metrics

data = pd.read_csv('../testdata/advertisement.csv')
print(data,data.info())

array = data.values
print(array[1])

x = array[:,0:4] # 슬라이싱
y = array[:,9]
y = y.astype('int')
# import sklearn.utils
# print(sklearn.utils.multiclass.type_of_target(y))

print(x.shape,x[:1], type(x))
print()
print(y.shape,y[0:10], type(y))
model = LogisticRegression()
model.fit(x,y)
y_hat = model.predict(x)
print('예측값 :',y_hat[:3])

f_value = model.decision_function(x)

df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f','y_hat','y'])
print(df)

print()
print(confusion_matrix(y, y_hat))

fpr, tpr, threshold = metrics.roc_curve(y,model.decision_function(x))
print('fpr :',fpr)
print('tpr :',tpr)
print('threshold (분류결정 임계값) :',threshold) # positive 예측값을 결정하는 확률 기준값

recall = 464 / (464 + 36)      # TP / (TP + FN)     # 재현률
fallout = 67 / (67 + 433)      # FP / (FP + TN)     # 위양성률

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