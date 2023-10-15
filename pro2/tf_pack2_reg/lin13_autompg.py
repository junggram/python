# AutoMPG dataset으로 자동차 연비 예측 모델

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from keras import layers

dataset = pd.read_csv('../testdata/auto-mpg.csv', na_values='?') 
# horsepwoer 칼럼이 '?' 때문에 object로 들어와서 na로 대체하여 float64 로 변경

print(dataset.head(2))
del dataset['car name'] # 칼럼 삭제
del dataset['model year'] # 칼럼 삭제
del dataset['origin'] # 칼럼 삭제
del dataset['acceleration'] # 칼럼 삭제
print(dataset.info())
print(dataset.corr()) # 피어슨 상관계수 확인

print(dataset.isna().sum()) # horsepower 6 
dataset = dataset.dropna() # 몇개 없어서 그냥 날려줌

# 시각화
sns.pairplot(dataset, diag_kind='kde')
# sns.pairplot(dataset[['mpg','cylinders','displacement','horsepower','weight','acceleration']], diag_kind='kde')
plt.show()

# train / test split
train_dataset = dataset.sample(frac=0.7, random_state=123)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset.shape, test_dataset.shape) # (274, 8) (118, 8)

# 표준화
train_stat = train_dataset.describe() # mean, std 확인해서 써먹으려고~
# print(train_stat)
train_stat.pop('mpg') # mpg는 label로 사용하려고 따로 뺌
train_stat = train_stat.transpose()
print(train_stat)

train_label = train_dataset.pop('mpg')
# print(train_label.head(2))
test_label = test_dataset.pop('mpg')
# print(test_label.head(2))

def st_func(x): # 표준화 함수
    return (x - train_stat['mean']) / train_stat['std']

print(st_func(10))
print(st_func(train_dataset[:3]))
st_train_data = st_func(train_dataset) # feature
st_test_data = st_func(test_dataset) # feature
print(st_train_data.columns)

print()
# model
from keras.models import Sequential
from keras.layers import Dense

def build_model():
    network = Sequential([
            Dense(units=64, activation='relu', input_shape=[4]),
            Dense(units=64, activation='relu'),
            Dense(units=1, activation='linear')
        ])
    
    opti = tf.keras.optimizers.RMSprop(0.001)
    network.compile(optimizer = opti, loss = 'mean_squared_error',
                     metrics=['mean_absolute_error','mean_squared_error'])
    
    return network

model = build_model()
print(model.summary())

# fit() 전에 모델을 실행해도 됨. 다만 성능은 기대하지 않음
print(model.predict(st_train_data[:1])) # 학습이 되지 않았기 때문에 의미 없는 데이터

epochs = 1000   # 조기종료를 시킬 수 있기 때문에 에폭수는 커도 무관
early_stop = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', mode='auto', patience=5) 
# validation가 학습을 검정하기 위한 데이터이기 때문에 일반 loss 말고 val_loss를 모니터링 해서 조기종료 시점을 정하자
# 자동 모드
# 감지 횟수 5회 = val_loss 가 5회 연속으로 떨어지지 않을 때 (오르락내리락 할 때)

history = model.fit(st_train_data, train_label, batch_size=32, epochs=epochs,
                    validation_split=0.2, verbose=2, callbacks=early_stop)

df = pd.DataFrame(history.history) # 결과를 쉽게 확인하기 위해서 DataFrame에 담아봄
print(df)
'''
Epoch 75/1000

70    6.738575  ...               13.836288
71    6.737248  ...               14.326653
72    6.857850  ...               13.940398
73    6.603187  ...               14.352324
74    6.724454  ...               13.935840
'''

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch
  
  plt.figure(figsize=(8,12))
  plt.subplot(2,1,1)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [MPG]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],label = 'Val Error')
  plt.legend()
  
  plt.subplot(2,1,2)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$MPG^2$]')
  plt.plot(hist['epoch'], hist['mean_squared_error'],label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],label = 'Val Error')
  plt.legend()
  
  plt.show()
  
plot_history(history)

# 모델 평가
loss, mae, mse = model.evaluate(st_test_data, test_label)
print('loss : {:5.3f}'.format(loss))
print('mae : {:5.3f}'.format(mae))
print('mse : {:5.3f}'.format(mse))

from sklearn.metrics import r2_score
print('설명력 : {:5.3f}'.format(r2_score(test_label, model.predict(st_test_data))))