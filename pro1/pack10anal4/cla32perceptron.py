# Perceptron(퍼셉트론, 단중신경망)이 학습할 때 주어진 데이터를 학습하고 에러가 발생한 데이터에 기반하여 Weight(가중치)값을 
# 기존에서 새로운 W값으로 업데이트 시켜주면서 학습을 하게 된다. input의 가중치합에 대해 임계값을 기준으로 
# 두 가지 output 중 한 가지를 출력하는 구조.

# 논리회로로 실습
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score


feature = np.array([[0,0], [0,1], [1,0], [1,1]])
print(feature)
# label = np.array([0,0,0,1]) # and(gate)
# and(gate) - 입력 두 개, 출력 하나 / 진리표 - [0,0,0,1]
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor

ml = Perceptron(max_iter=10, eta0=0.1, verbose=1).fit(feature, label) # max_iter=10 학습 횟수
print(ml)
pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))

