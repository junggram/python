# 방법 4 : linregress를 사용 . model O

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# iq에 따른 시험점수 예측
score_iq = pd.read_csv('../testdata/score_iq.csv')
print(score_iq.head(3))
print(score_iq.info()) # iq와 score의 data type이 모두 int     # 회귀분석 사용 가능

print(score_iq.corr()) # corr() = 상관계수

x = score_iq['iq']  
y = score_iq['score']

print(np.corrcoef(x,y)[0,1]) # 0.8822203446134707 양의 상관관계

# plt.scatter(x, y)
# plt.show()

# 모델 생성
model = stats.linregress(x, y)
print(model) # slope=0.6514309527270081, intercept=-2.856447122197551, rvalue=0.8822203446134705, pvalue=2.8476895206672287e-50, stderr=0.028577934409305377, intercept_stderr=3.54621191804853
print('slope :',model.slope) # 하나씩 볼 수도 있음
print('intercept :',model.intercept) # 하나씩 볼 수도 있음
print('r-value :',model.rvalue) # 하나씩 볼 수도 있음
print('p-value :',model.pvalue) # 하나씩 볼 수도 있음 #  2.8476895206672287e-50 < 0.05 회귀모델은 유의하다, 두 변수간에 인과관계가 있다
print('stderr :',model.stderr) # 하나씩 볼 수도 있음
    
# y_hat = 0.6514309527270081 * x + -2.856447122197551

plt.scatter(x,y)
plt.plot(x, model.slope * x + model.intercept,c = 'red')
plt.show()

# 점수 예측
print('점수 예측 :',model.slope * 140 + model.intercept) # 회귀식을 이용해 예측값을 구해본다
print('점수 예측 :',model.slope * 120 + model.intercept) # 회귀식을 이용해 예측값을 구해본다
print('점수 예측 :',model.slope * 90 + model.intercept) # 회귀식을 이용해 예측값을 구해본다
print() # linregress 는 predict를 지원하지 않음
new_df = pd.DataFrame({'iq':[140,130,120,110,100]})
print('점수 예측 :',np.polyval([model.slope,model.intercept],new_df)) # np.polyval() 을 통해서 예측값을 구함, 여러개의 예측값을 한번에 구할 수 있음

