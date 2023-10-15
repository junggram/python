# [XGBoost 문제] 
#
# kaggle.com이 제공하는 'glass datasets'
#
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7 가지의 label(Type)로 분리된다.
#
# RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
#  Type
#
#                           ...
#
# glass.csv 파일을 읽어 분류 작업을 수행하시오.

import pandas as pd
import xgboost as xgb

data = pd.read_csv('../testdata/glass.csv')
# print(data.head(3), data.shape)

features = data.iloc[:,:9]
labels = data.iloc[:,9]
print(features)
print(labels, set(labels), labels.unique())

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.3, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (149, 9) (65, 9) (149,) (65,)

le = LabelEncoder()
y_train = le.fit_transform(y_train) # 레이블 인코더로 y값을 맞춰줌

model = xgb.XGBClassifier(n_estimators = 500, random_state=12).fit(x_train, y_train)
pred = model.predict(x_test)

print('예측값 :', pred[:5]) # 예측값 : [1 1 4 0 5]
print('실제값 :', np.array(y_test[:5])) # 실제값 : [2 2 6 1 7]
print('분류정확도 :', accuracy_score(y_test, pred)) # 분류정확도 : 0.092

xgb_roc_curve = roc_auc_score(y_test, model.predict_proba(x_test), multi_class='ovr')
print('ROC AUC : {0:.4f}'.format(xgb_roc_curve)) # ROC AUC : 0.9565

from xgboost import plot_importance
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier

fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(model, ax = ax)
plt.show()