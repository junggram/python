# 원격 데이터베이스 연동 프로그램
# pip install mysqlclient

import MySQLdb

# conn=MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close()

#sangdata table 과 연동

config = { # 위처럼 한줄로 써도 되고 이렇게 써도 된다
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn= MySQLdb.connect(**config)
    # print(conn)
    cursor=conn.cursor()
    
    '''# insert 문
    # sql="insert into sangdata(code, sang, su, dan) values (5,'쎄무점퍼',1,78000000)"
    # cursor.execute(sql)
    sql="insert into sangdata values (%s,%s,%s,%s)"
    sql_data = '12','호경재킷','1','100000000'
    cursor.execute(sql,sql_data)
    #count = cursor.execute(sql,sql_data)
    #print(count)
    conn.commit()'''
    
    '''# update 문
    sql="update sangdata set sang=%s, su=%s where code=%s"
    sql_data=('파이썬',5,11)
    count = cursor.execute(sql,sql_data)
    print(count)
    conn.commit()'''
    
    '''# delete 문
    code = '11'
    #sql = "delete from sangdata where code="+code # secure coding 가이드라인에 위배됨
    #sql = "delete from sang data where code='{0}'".format(code)
    #cursor.execute(sql)
    sql = "delete from sangdata where code=%s"
    cursor.execute(sql,(code,))
    conn.commit()'''
    
    # select 문
    sql="select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    # 방법1 (select 한 data를 읽어오는)
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
        
    # 방법2
    print()
    for r in cursor:
        #print(r)
        print(r[0],r[1],r[2],r[3])
        
    #방법3
    print()
    for (code,sang,su,dan) in cursor: # (code,sang,su,dan) 는 칼럼명이 아니고 단순 변수명이기 때문에 DB의 칼럼명과 달라도 된다
        print(code,sang,su,dan) # (code,sang,su,dan) 는 칼럼명이 아니고 단순 변수명이기 때문에 DB의 칼럼명과 달라도 된다
        
except Exception as e:
        print('에러: '+e)
finally:
    cursor.close()
    conn.close()