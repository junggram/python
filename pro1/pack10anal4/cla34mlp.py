# MLP(다층 신경망)

# 논리회로로 실습
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


feature = np.array([[0,0], [0,1], [1,0], [1,1]])
print(feature)
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor

# model = MLPClassifier(hidden_layer_sizes=5, solver='adam', learning_rate_init = 0.01).fit(feature, label)
# model = MLPClassifier(hidden_layer_sizes=30, solver='adam', learning_rate_init = 0.1,
#                       max_iter=10, verbose=1).fit(feature, label)
model = MLPClassifier(hidden_layer_sizes=(10,10,10), solver='adam', learning_rate_init = 0.1,
                      max_iter=10, verbose=1).fit(feature, label)

pred = model.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))

