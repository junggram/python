import MySQLdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import csv

# pandas 문제 5)
# a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.

#      - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

try:
    with open('mydb.dat',mode='rb') as obj:
        config=pickle.load(obj)
except Exception as e:
    print('connect err: ',e) 
 
 
try: 
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    sql="""
        select jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    
    df1=pd.DataFrame(cursor.fetchall(),
                     columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_pay', 'jikwon_jik'])
    print(df1.head(3))
    
#      - DataFrame의 자료를 파일로 저장
    df1.to_csv('문제5.csv')
    
#      - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    buser_pay=df1.groupby(['buser_name'])['jikwon_pay']
    print('부서별 연봉 합:',buser_pay.sum())
    print('부서별 연봉 최대:',buser_pay.max())
    print('부서별 연봉 최소:',buser_pay.min())
    
#      - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
    cst=pd.crosstab(df1['buser_name'],df1['jikwon_jik'],margins=2)
    print(cst)
    
#      - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    sql="""
        select j.jikwon_name, g.gogek_no, g.gogek_name, g.gogek_tel
        from jikwon j left outer join gogek g
        on j.jikwon_no=g.gogek_damsano
    """
    cursor.execute(sql)
    
    df2=pd.DataFrame(cursor.fetchall(),
                     columns=['직원이름','고객번호','고객명','고객전화'])
    
    for i in df2.columns:
        df2['고객명']=df2['고객명'].fillna('담당 고객 X')
        df2[i]=df2[i].fillna(' ')
    print(df2)
    
#      - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    data = []
    for i in buser_pay.mean():
        data.append(i)
    plt.barh(buser_pay.mean().index,data) # 가로막대
    plt.show()
    
# b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
    sql="""
        select jikwon_gen, jikwon_pay
        from jikwon
    """
    cursor.execute(sql)
    
    df=pd.DataFrame(cursor.fetchall(),
                    columns=['성별','연봉'])
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
    mean=pd.pivot_table(df, values=['연봉'], index=['성별'])
    print(mean)
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
    data = []
    for i in mean.values():
        data.append(i)
    plt.bar(mean.index,data) # 세로 막대
    plt.show()
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))    
    
except Exception as e:
    print('process err: ',e)
finally:
    cursor.close()
    conn.close()

