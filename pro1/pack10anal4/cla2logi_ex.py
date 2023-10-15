# [로지스틱 분류분석 문제1]
#
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.


from io import StringIO
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

data = StringIO('''
요일,외식유무,소득수준
토,0,57
토,0,39
토,0,28
화,1,60
토,0,31
월,1,42
토,1,54
토,1,65
토,0,45
토,0,37
토,1,98
토,1,60
토,0,41
토,1,52
일,1,75
월,1,45
화,0,46
수,0,39
목,1,70
금,1,44
토,1,74
토,1,65
토,0,46
토,0,39
일,1,60
토,1,44
일,0,30
토,0,34
'''   )

data = pd.read_csv(data, dtype={'요일':'string'})
data = data[(data['요일'] == '토')|(data['요일'] == '일')] # 토요일과 일요일만 뽑아냄

my_formula = '외식유무 ~ 소득수준'
print(my_formula)
model = smf.glm(formula = my_formula, data = data, family = sm.families.Binomial()).fit()
pred = model.predict(data)
print(model.summary())  

from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(data['외식유무'], np.around(pred)))

new_input_data = pd.DataFrame({'소득수준':[int(input('소득수준 : '))]})
print('외식 유무 :', np.rint(model.predict(new_input_data)))
print('외식을 함' if np.rint(model.predict(new_input_data))[0] == 1 else '외식안함')