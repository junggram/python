# Two-way ANOVA (이원분산분석) : 요인 복수 - 각 요인의 그룹도 복수

import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm

plt.rc('font',family='malgun gothic')

url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt'
data = pd.read_csv(urllib.request.urlopen(url))

print(data.head(3),data.shape)
print()

# data.boxplot(column='머리둘레', by='태아수')
# plt.show()
#
# data.boxplot(column='머리둘레', by='관측자수')
# plt.show()

# 귀무 : 태아수와 관측자수는 태아의 머리 둘레와 관련이 없다
# 대립 : 태아수와 관측자수는 태아의 머리 둘레와 관련이 있다

# 태아수와 관측자수의 상호작용을 빼고 검정한 경우
reg = ols('data["머리둘레"] ~ C(data["태아수"]) + C(data["관측자수"])',data=data).fit()
result = anova_lm(reg, typ=1)
print(result)

#===============================================================================
 
#                    df      sum_sq     mean_sq            F        PR(>F)
# C(data["태아수"])    2.0  324.008889  162.004444  2023.182239  1.006291e-32
# C(data["관측자수"])   3.0    1.198611    0.399537     4.989593  6.316641e-03
# Residual         30.0    2.402222    0.080074          NaN           NaN

#===============================================================================




# 태아수와 관측자수의 상호작용(교호작용)을 포함해서 검정한 경우                 # C(data["태아수"]) : C(data["관측자수"])
reg2 = ols('data["머리둘레"] ~ C(data["태아수"]) + C(data["관측자수"]) + C(data["태아수"]) : C(data["관측자수"])',data=data).fit()
result2 = anova_lm(reg2, typ=1)
print(result2)
# 해석 : p-value 3.295509e-01 > 0.05 이므로 귀무가설 채택
# 태아수와 관측자수는 태아의 머리둘레와 관련이 없다

#===============================================================================
                                  # df      sum_sq  ...            F        PR(>F)
# C(data["태아수"])                   2.0  324.008889  ...  2113.101449  1.051039e-27
# C(data["관측자수"])                  3.0    1.198611  ...     5.211353  6.497055e-03
# C(data["태아수"]):C(data["관측자수"])   6.0    0.562222  ...     1.222222  3.295509e-01
# Residual                        24.0    1.840000  ...          NaN           NaN

#===============================================================================