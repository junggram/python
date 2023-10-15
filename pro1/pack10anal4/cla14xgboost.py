# XGBoost 로 분류 모델 작성
# breast_cancer dataset 사용
# pip install xgboost
# pip install lightgbm

import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
import xgboost as xgb
from sklearn.model_selection import train_test_split
from xgboost import plot_importance
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier  # xgboost보다 성능이 우수함. 대용량 처리에 효과적. 데이터가 적으면 과적합 발생 우려 매우 높음
from sklearn import metrics

dataset = load_breast_cancer()

x_feature = dataset.data
y_label = dataset.target

cancer_df = pd.DataFrame(data=x_feature, columns=dataset.feature_names)
print(cancer_df.head(5), cancer_df.shape) # (569, 30)
print(dataset.target_names) # malignant : 양성, benign : 음성
print(np.sum(y_label == 0)) # 양성 : 212
print(np.sum(y_label == 1)) # 음성 : 357

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size = 0.2, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (455, 30) (114, 30) (455,) (114,)

# 모델
model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators=500 ).fit(x_train, y_train)
# model = LGBMClassifier().fit(x_train, y_train) # 개량종으로 별도 지원이 되는 LGBMClassifier 로도 모델 만들기 가능
print(model)
pred = model.predict(x_test)
print('예측값 :',pred[:10]) # 예측값 : [0 1 1 1 1 1 1 1 1 0]
print('실제값 :',y_test[:10]) # 실제값 : [0 1 1 1 1 1 0 1 1 0]
print('분류 정확도 :',metrics.accuracy_score(y_test, pred)) # 분류 정확도 : 0.9473

print()
cl_rep = metrics.classification_report(y_test,pred)
print('classification_report :\n', cl_rep)

# 중요 변수 시각화
# fig, ax = plt.subplots(figsize = (10, 12))
# plot_importance(model, ax = ax)
# plt.show()