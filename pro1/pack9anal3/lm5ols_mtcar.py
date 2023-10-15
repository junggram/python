# # mtcars dataset 으로 단순 / 다중 회귀모델 작성 : ols() 사용
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import statsmodels.api
# plt.rc('font', family = 'malgun gothic')
# import seaborn as sns
# import statsmodels.formula.api as smf
#
# mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
# print(mtcars.head(3))
# # print(mtcars.corr())
# print(np.corrcoef(mtcars.hp,mtcars.mpg)) # -0.77616837
# print(np.corrcoef(mtcars.wt,mtcars.mpg)) # -0.86765938
#
# # 단순 선형회귀 : mtcars.hp(feature, x), mtcars.mpg(label, y) 마력수가 연비에 영향을 준다는 가정하에 모델 작성
#
# # 시각화
# '''plt.scatter(mtcars.hp, mtcars.mpg)
# # 참고 : numpy 의 polyfit()을 이용하면 slope와 intercept를 얻을 수 있다
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg,1)
# print('slope:{}, intercept:{}'.format(slope,intercept)) # slope:-0.0682, intercept:30.0988
# plt.plot(mtcars.hp, slope * mtcars.hp + intercept, color='r')
# plt.xlabel('마력수')
# plt.ylabel('연비')
# plt.show()'''
#
# result1 = smf.ols(formula = 'mpg ~ hp',data = mtcars).fit()
# print(result1.summary())
# print()
# print(result1.summary().tables[1]) # 요약표의 아래만 볼수도 있다
#
# print('마력수 110에 대한 연비는 :',-0.0682*110+30.0989)
# print('마력수 50에 대한 연비는 :',-0.0682*50+30.0989)
# print('마력수 200에 대한 연비는 :',-0.0682*200+30.0989)
#
# print('------------------------')
# # 다중 선형회귀 : mtcars.hp, mtcars.wt (feature, x), mtcars.mpg (label, y)
# result2 = smf.ols(formula = 'mpg~hp+wt', data=mtcars).fit()
# print(result2.summary())
# print('마력수 110, 차체 무게5톤에 대한 연비는 :',(-0.0318*110)+(-3.8778*5) + 37.2273)
#
# print('predict 함수 사용')
# new_hp = float(input('새로운 마력수 : '))
# new_wt = float(input('새로운 차체무게 : '))
# new_Data = pd.DataFrame({'hp':[new_hp],'wt':[new_wt]})
# new_pred = result2.predict(new_Data)
# print('예상 연비 :', new_pred.values)
#
# new_Data2 = pd.DataFrame({'hp':[100,120,150],'wt':[5,2,7]})
# new_pred2 = result2.predict(new_Data2)
# print('예상 연비 :', new_pred2.values)

# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api
plt.rc('font', family = 'malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf

data = pd.read_csv('../testdata/student.csv')
print(data.head(3))

print(data.corr())

re1 = smf.ols(formula = '수학~국어', data=data).fit()
print(re1.summary()) # Prob (F-statistic):8.16e-05, R-squared:0.587
new_gook = float(input('국어 점수 : '))
new_Data = pd.DataFrame({'국어':[new_gook]})
pr1 = re1.predict(new_Data)
print('예상 수학점수 :', pr1.values)

new_Data2 = pd.DataFrame({'국어':[90]})
new_pred2 = re1.predict(new_Data2)
print('예상 수학점수 :', new_pred2.values)

re2 = smf.ols(formula = '수학 ~ 국어 + 영어',data=data).fit()
print(re2.summary()) # Prob (F-statistic):0.000105, Adj. R-squared:0.619
new_gook = float(input('국어 점수 : '))
new_eng = float(input('영어 점수 : '))
new_Data = pd.DataFrame({'국어':[new_gook],'영어':[new_eng]})
new_pred = re2.predict(new_Data)
print('예상 수학점수 :', new_pred.values)

new_Data2 = pd.DataFrame({'국어':[90],'영어':[100]})
new_pred2 = re2.predict(new_Data2)
print('예상 수학점수 :', new_pred2.values)
