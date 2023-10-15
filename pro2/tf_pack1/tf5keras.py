# Keras 라이브러리(모듈)로 모델 생성 네트워크 구성하기

'''
Keras 기본 개념 
  - 케라스의 가장 핵심적인 데이터 구조는 "모델" 이다.
  - 케라스에서 제공하는 시퀀스 모델을 이용하여 레이어를 순차적으로 쉽게 쌓을 수 있다. 
  - 케라스는 Sequential에 Dense 레이어(fully-connected layers 완전히 연결된 레이어)를 쌓는 스택 구조를 사용한다.
'''




import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Activation # 뉴런의 출력값을 결정하는 Activation Function(활성화함수)
from keras.optimizers import SGD, RMSprop, Adam

# 논리회로 분류 모델 생성 
# 1) 데이터 수집 및 가공
x = np.array([[0,0],[0,1],[1,0],[1,1]])
print(x)
y = np.array([0,1,1,1]) # or






# 2) 모델 네트워크 구성
# 시퀀스 모델을 생성한 뒤 필요한 레이어를 추가하며 구성한다. ( add()를 사용해도 되고, Sequential 안에 정의해도 된다 )
'''
model = Sequential()                                  # 모델 설정
model.add(Dense(units=1, input_dim=2))                # 레이어 추가       # 2개로 들어와서 1개로 빠져나감
model.add(Activation('sigmoid'))                      # 레이어 추가       # 활성화함수 (시그모이드) 설정
'''
model = Sequential([
    Dense(units = 1, input_dim = 2),
    Activation('sigmoid')
    ])








# 3) 모델 학습 과정 설정
# 학습하기 전, 학습에 대한 설정을 수행한다. 손실 함수 및 최적화 방법을 정의. compile() 함수를 사용
# model.compile(optimizer = 'sgd', loss = 'binary_crossentropy', metrics = ['accuracy']) 
                                                               # loss function = cost function (손실 함수 : 기울기를 구하기 위해 사용)
                                                               # loss = 'binary_crossentropy' : 이항분류 일 때 사용하는 loss function
                                                               # metrics = ['accuracy'] : 이항분류이기 때문에 accuracy(정확도) 계산
                                                               
                                                               # optimizer, loss, metrics 는 필수요소이기 때문에 꼭 입력을 해주자.
# 학습 스텝의 크기는 learning_rate : 작을수록 세밀하게 움직인다
# verbose를 보고 loss값이 조금씩 떨어지면 늘려주고, 많이씩 떨어지면 줄여준다.
''' # 확률적 경사 하강법 : SGD                                 
model.compile(optimizer = SGD(learning_rate = 0.01, momentum=0.9), # 경사 하강법에 momentum을 사용해 관성을 줘서 국소최적해(Local minimum)에서 벗어날 수 있다,
                                                                   # momentum을 주지 않으면 Local minimum을 Global minimum으로 착각해서
                                                                   # cost값이 크게 나와서 예측값과 실제값의 차이가 커질 수 있다
               loss = 'binary_crossentropy',
                metrics = ['accuracy'])                               
'''
# model.compile(optimizer = RMSprop(learning_rate=0.001), loss = 'binary_crossentropy', metrics = ['accuracy']) 
model.compile(optimizer = Adam(learning_rate=0.001), loss = 'binary_crossentropy', metrics = ['accuracy']) 







# 4) 모델 학습시키기 - Machine Learning에서 학습이란? : 더 나은 표현(출력)을 찾는 자동화 과정 (최적화 모델을 찾는 과정)      
# 훈련셋을 이용하여 구성한 모델로 학습을 시킨다. fit() 함수 사용
model.fit(x, y, batch_size=1, # batch_size : 훈련데이터를 여러개의 작은 묶음으로 만들어줌
           epochs=1000, # 학습 반복 횟수
            verbose = 0, # 학습 과정을 안보여줌, 보여줌 = 1, 조금만 보여줘 = 2
             )
#---






# 5) 모델 평가
# train / test data를 사용해야하지만 지금은 데이터가 적기 때문에 안하고 그냥 사용
# 준비된 시험셋으로 학습한 모델을 평가한다. evaluate() 함수를 사용
loss_metrics = model.evaluate(x = x, y = y, 
                               batch_size = 1,
                                verbose = 0)
print('loss_metrics :', loss_metrics) # loss_metrics : [0.6607667803764343, 0.5] = [ loss, accuracy ]
                                      # 고정된 값이 아님 달라질 수 있음 - w와 b값이 랜덤하기 때문에
                                      # 현재는 반복 학습의 횟수가 낮기 때문에 변동이 크당 ㅎㅎ 반복학습의 횟수가 늘어날수록 accuracy가 늘어남
#---






# 6) 모델 사용 - 예측값 출력
# 임의의 입력으로 모델의 출력을 얻는다. predict() 함수를 사용
pred = model.predict(x = x, batch_size = 1, verbose = 0)
print('pred :', pred)
print('pred :', pred.flatten()) # flatten() : 차원 축소~
pred = (model.predict(x) > 0.5).astype('int32') # 0.5를 기준으로  1 or 0 으로 분류
print('pred :', pred)







# 7) 최적의 모델이 만들어졌다면 ? - 모델 저장 후 읽기

model.save('tf5.hdf5') # 모델 저장 
                       # hdf5 : 대용량 데이터 라는 뜻의 확장자 (R에서도 쓰고, 파이썬에도 쓴다)
                       # 굳이 이렇게 안줘도 되지만, 그냥 사람들이 대용량데이터는 이 확장자로 많이 씀

del model # 모델 삭제

from keras.models import load_model
model = load_model('tf5.hdf5')
pred = (model.predict(x) > 0.5).astype('int32')
print('pred :', pred)