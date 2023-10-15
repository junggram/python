'''
import pandas as pd
from sklearn.model_selection._split import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data = pd.read_csv("../testdata/bodycheck.csv")
print(data.head(2))
x = data[["게임","TV시청"]]
y = data["안경유무"]
x = x.values  # matric
y = y.values  # vector
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) 
print(x_train.shape, x_test.shape) 

model = LogisticRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(pred)

import numpy as np
new_data = np.array([[3,3]])

pred2 = model.predict(new_data)

if pred2 == 1:
    print('게임 시간이 {0}이고 TV시청 시간이 {1}인 경우 안경 착용 O'.format(new_data[:,0][0],new_data[:,1][0]))
else : 
    print('게임 시간이 {0}이고 TV시청 시간이 {1}인 경우 안경 착용 X'.format(new_data[:,0][0],new_data[:,1][0]))
'''



'''
# 단일표본 검정(one-sample t-test)에 대한 문제다. 남아 신생아 몸무게의 평균 검정을 수행하려고 한다.
# 파일명 : babyboom.csv (testdata 폴더에 있음) # 1:여아, 2:남아
# 남아 신생아의 몸무게는 평균이 3000(g)으로 알려져 왔으나 이것이 틀렸다는 주장이 나왔다.
# 귀무, 대립 가설을 적고, 표본으로 남아를 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정하는 코드를 작성하시오.


# 귀무 : 남아 신생아의 몸무게는 평균이 3000(g)이다
# 대립 : 남아 신생아의 몸무게는 평균이 3000(g)이 아니다

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('../testdata/babyboom.csv')
# print(data)

data = data[data['gender']==2]
print(data)

result = stats.ttest_1samp(data['weight'], popmean=3000)
print('result : statistic(t-value):{}, p-value:{}'.format(result[0],result[1]))
# 해석 : p-value:0.00014690 < 0.05 이므로 귀무가설 기각, 남아 신생아의 몸무게는 평균이 3000(g)이 아니다
'''



'''
import numpy as np

# 지각횟수(x) = 1, 2, 3, 4, 5
# 판매횟수(y) = 8, 7, 6, 4, 5

x= [1,2,3,4,5]
y= [8,7,6,4,5]

print(np.corrcoef(x,y))
'''




import pandas as pd

data = pd.read_csv('../testdata/titanic_data.csv', usecols=['Survived', 'Pclass', 'Sex', 'Age','Fare'])
print(data.head(2), data.shape) # (891, 12)
data.loc[data["Sex"] == "male","Sex"] = 0
data.loc[data["Sex"] == "female", "Sex"] = 1
print(data["Sex"].head(2))
print(data.columns)

feature = data[["Pclass", "Sex", "Fare"]]
label = data["Survived"]

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(feature, label,test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print('분류 정확도 :',accuracy_score(y_test, pred))