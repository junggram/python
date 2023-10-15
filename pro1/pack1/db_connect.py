# 마리아DB 연결 정보를 객체로 저장

config = { # 위처럼 한줄로 써도 되고 이렇게 써도 된다
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

import pickle

with open('mydb.dat',mode='wb') as obj:
    pickle.dump(config,obj)