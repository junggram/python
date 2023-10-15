# 원갹 DB와 연동 후 DataFrame 으로 처리

import MySQLdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import csv

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
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    #출력1: DataFrame으로 출력
    df1=pd.DataFrame(cursor.fetchall(),
                     columns=['jikwon_no', 'jikwon_name', 'buser_name','jikwon_jik', 'jikwon_gen', 'jikwon_pay'])
    print(df1.head(3))
    
    #출력1: csv파일
    with open("직원.csv", mode='w', encoding='utf-8-sig') as fo:
        writer=csv.writer(fo) #write객체를 만들고
        for r in cursor:
            writer.writerow(r)
            
    #직원 csv 읽기
    df2=pd.read_csv('직원.csv')
    print(df2.head(3))
    
    print('pandas 지원 sql 사용') # pandas sql
    df = pd.read_sql(sql,conn)
    df.columns = ['번호','이름','부서','직급','성별','연봉']
    print(df.head(3))
    print()
    print('건수',len(df),df['이름'].count())
    print('직급 별 인원수 :', df['직급'].value_counts())
    print('연봉 평균 :', df.loc[:,'연봉'].mean())
    print('표준 편차 :',df.loc[:,'연봉'].std())
    
    # 교차표
    ctab = pd.crosstab(df['성별'], df['직급'], margins=True) 
    print(ctab)
    
    # 시각화 : 직급별 연봉 평균
    jik_ypay=df.groupby(['직급'])['연봉'].mean()
    print(jik_ypay,type(jik_ypay))
    print(jik_ypay.index)
    print(jik_ypay.values)
    
    plt.pie(jik_ypay, explode=(0.2,0,0,0.3,0), labels=jik_ypay.index, shadow=True, 
            labeldistance=0.7, counterclock=False)
    plt.show()
    
except Exception as e:
    print('process err: ',e)
finally:
    cursor.close()
    conn.close()


