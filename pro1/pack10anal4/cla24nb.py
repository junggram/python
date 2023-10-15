# 나이브 베이즈는 분류기를 만들 수 있는 간단한 기술로써 단일 알고리즘을 통한 훈련이 아닌 일반전깅 원칙에 근거한
# 여러 알고리즘들을 이용하여 훈련된다. 모든 나이브베이즈 분류기는 공통적으로 모든 특성값은 서로 독립임을 가정한다
# 예를 들어, 특정 과일을 사과로 분류 가능하게 하는 특성들(둥글다, 빨갛다, 지름10cm) 은 나이브 베이즈 분류기에서
# 특성들 사이에 발생할 수 있는 연관성이 없음을 가정하고 각각의 특성들이 특정 과일이 아닌 사과일 확률에 독립저긍로 기여 하는 것으로 간주한다

from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics

# 조건부 확률   P(Label | Feature) = P(Feature | Label) * P(Label) / P(Feature)

x=np.array([1,2,3,4,5])
x = x[:, np.newaxis]
print(x)
y = np.array([1,3,5,7,9])
model = GaussianNB().fit(x,y)
print(model)
pred = model.predict(x)
print('분류 정확도 :', metrics.accuracy_score(y, pred))

# 새로운 값으로 예측
new_x = np.array([[0.1], [0.5], [5], [12]])
new_pred = model.predict(new_x)
print('새로운 예측 값 :', new_pred)