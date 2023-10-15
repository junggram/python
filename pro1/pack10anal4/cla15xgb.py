# 산탄데르 은행 고객 만족 여부 분류 모델
# label name : TARGET - 0(만족), 1(불만족)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df = pd.read_csv('../testdata/train.csv', encoding='latin-1')
print(df.head(3), df.shape) # (76020, 371)
print(df.info())
print()
print(df['TARGET'].value_counts())
unsatisfied_cnt = df[df['TARGET']==1].TARGET.count()
total_cnt = df.TARGET.count()
print('불만족 비율 : {0:.2f}'.format(unsatisfied_cnt/total_cnt)) # 불만족 비율 : 0.04
# pd.set_option('display.max_columns',500)
print(df.describe())
df['var3'].replace(-999999, 2, inplace = True) # 아웃라이어 대체
# print(df.describe())
df.drop('ID', axis=1, inplace=True)

x_features = df.iloc[:,:-1]
y_labels = df.iloc[:,-1]

# train / test split
x_train, x_test,y_train, y_test = train_test_split(x_features, y_labels,test_size=0.2, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

train_cnt = y_train.count()
test_cnt = y_test.count()
print('train 데이터 레이블 분포 비율 : ', y_train.value_counts() / train_cnt) # 0 : 0.960257, 1 : 0.039743
print('test 데이터 레이블 분포 비율 : ', y_test.value_counts() / test_cnt) # 0 : 0.961129, 1 : 0.038871

# 모델 
import xgboost as xgb
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score

xgb_clf = xgb.XGBClassifier(n_estimators = 5, random_state=12).fit(x_train, y_train, eval_metric='auc', early_stopping_rounds = 2, eval_set=[(x_train, y_train), (x_test, y_test)])
xgb_clf.predict(x_test)

xgb_roc_curve = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:,1])
print('ROC AUC : {0:.4f}'.format(xgb_roc_curve)) # ROC AUC : 0.8399
pred = xgb_clf.predict(x_test) 
print('예측값 :', pred[:5]) # 예측값 : [0 0 0 0 0]
print('실제값 :', y_test[:5].values) # 실제값 : [0 0 0 0 0]
print('분류정확도 :', accuracy_score(y_test, pred)) # 분류정확도 : 0.9611

# GridSearchCV 로 best parameter 를 구한 후 모델 작성
# 중요 변수를 알아내 feature를 줄이는 작업을
# 성격이 유사한 변수들에 대해 자원축소를 하여 feature를 줄이는 작업
# ...

