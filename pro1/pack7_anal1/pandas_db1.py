# local DB와 pandas

import sqlite3
import pandas as pd

sql = 'create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)'
conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('mydb')
conn.execute(sql)
conn.commit()

datas = [('mouse', 'samsong', 12.5, 5000), ('keyboard','alg',12.5,5000)]
stmt = 'insert into test values(?,?,?,?)'
conn.executemany(stmt, datas) # 여러개를 한번에 입력 executemany

data1 = ('monitor','abc',100.0,550000) 
conn.execute(stmt,data1) # 한개만 입력 execute

conn.commit()

cursor = conn.execute('select * from test')
rows = cursor.fetchall()

for a in rows:
    print(a)
    
# DataFrame에 자료를 기억
df1 = pd.DataFrame(rows, columns=['product','maker','weight','price'])
print(df1)

print()
# Pandas의 SQL 기능을 사용 !!!!!!!!!!!!!!!!!!!!!!
df2 = pd.read_sql('select * from test', conn)
print(df2)

print()
# DataFrame의 자료를 DB로 저장
data = {
    'product':['김시네','정대정','윤성현'],
    'maker':['모나미','모났니','모나왔니'],
    'weight':[2.3,5.5,12.0],
    'price':[500,1500,1000]
    }

frame = pd.DataFrame(data)
print(frame)

print('---------------------')
frame.to_sql('test',conn,if_exists='append',index=False) # 이미 테이블이 있으면 추가
df3 = pd.read_sql('select * from test',conn)
print(df3)

print()
print(pd.read_sql('select count(*) as 건수 from test',conn))