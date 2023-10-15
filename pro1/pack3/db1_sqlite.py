# sql lite3 : 파이썬 기본 개인용 DB

import sqlite3
print(sqlite3.sqlite_version)

print()
# conn = sqlite3.connect('exam.db')
conn = sqlite3.connect(':memory:') # 1회용 : ram에 일시적으로 data가 저장이 된다 (실험용)
try:
    cursor=conn.cursor()    # SQL문 처리
    
    # table 생성
    cursor.execute("create table if not exists fritab(name text, phone text)") #SQL 문은 '보다 "로 감싸자 
    
    # 자료 추가
    cursor.execute("insert into fritab(name, phone) values('한국인', '111-0000')")
    cursor.execute("insert into fritab values('우주인', '000-1111')")
    cursor.execute("insert into fritab values(?, ?)", ('신기해','123-4567'))
    inputdata=('신기루','987-6543')
    cursor.execute("insert into fritab values(?, ?)", inputdata)
    conn.commit() # 커밋
    
    # select
    cursor.execute("select * from fritab")
    print(cursor.fetchone()) # 하나만 읽어오기
    print(cursor.fetchall()) # 전체 읽어오기 , list형식으로 반환
except Exception as e:
    print('에러: '+e)
    conn.rollback() # 에러시 되돌리기
finally:
    conn.close()
