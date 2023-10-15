# DataFrame의 재구조화 : stack / unstack

import numpy as np
import pandas as pd

df = pd.DataFrame(1000+np.arange(6).reshape(2,3),
                  columns = ['2020','2021','2022'],
                  index = ['대전','서울'])
print(df)
print()
df_row = df.stack() # index를 기준으로 칼럼쌓기
# 대전  2020    1000
#      2021    1001
#      2022    1002
# 서울  2020    1003
#      2021    1004
#      2022    1005
print(df_row)

print()
df_col = df_row.unstack() # stack결과를 원래대로 되돌림, 인덱스를 열로 보내는 역할
#      2020  2021  2022
# 대전  1000  1001  1002
# 서울  1003  1004  1005
print(df_col)

print('------ 데이터 범주화 (연속형 => 범주형) ------')
price=[10.3, 5.5, 7.8, 3.6]
cut = [3,7,9,11] # 구간 기준값
result_cut = pd.cut(price, cut)
print(result_cut) # [(9, 11] = 9 < x <= 11,
#                    (3, 7] = 3 < x <= 7,...
print(pd.value_counts(result_cut)) # 범주화의 결과를 카운팅

print()
datas = pd.Series(np.arange(1,1001)) # 시리즈 DataFrame 아님
print(datas.head(2))
print(datas.tail(2))

# cut = [1,500,100] # 구간 기준값
# result_cut2 = pd.qcut(datas, cut) # 범주가 아주 많을 때
# print(result_cut2)

result_cut2 = pd.qcut(datas, 3)
print(result_cut2)
# 0       (0.999, 334.0]
# 1       (0.999, 334.0]
# 2       (0.999, 334.0]
# 3       (0.999, 334.0]
# 4       (0.999, 334.0]
#             ...       
# 995    (667.0, 1000.0]
# 996    (667.0, 1000.0]
# 997    (667.0, 1000.0]
# 998    (667.0, 1000.0]
# 999    (667.0, 1000.0]
# Length: 1000, dtype: category

print(pd.value_counts(result_cut2))
# (0.999, 334.0]     334
# (334.0, 667.0]     333
# (667.0, 1000.0]    333

print()
# 각 범주의 그룹별 연산
group_col= datas.groupby(result_cut2)
# print(group_col)

print(group_col.agg('count')) 
print(group_col.agg(['count','mean','std','min'])) # [ ]에 여러개의 연산을 한번에 요청할 수 있다

# 직접 함수를 작성하여 그룹별 연산
def summary_func(gr):
    return {
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min(),
        }
print(group_col.apply(summary_func)) # 함수를 실행하는 함수
print(group_col.apply(summary_func).unstack()) # group_col.agg(['count','mean','std','min']) 과 같은 모양

