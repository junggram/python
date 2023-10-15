# 키보드에서 부서번호를 입력 받아서 해당 부서 직원자료(사번, 이름, 부서,연봉,직급) 출력

import MySQLdb
import pickle

'''config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}'''

with open('mydb.dat',mode='rb') as obj: # 위 대신 mydb.dat로 내 db정보를 불러오는 것으로 (암호화 + 간편함)을 확보
    config =pickle.load(obj)

def chulbal():
    try:
        conn= MySQLdb.connect(**config) # dict 이기때문에 **config
        # print(conn)
        cursor=conn.cursor()
        buser_info = input('부서이름 : ')
        
        sql="""
            select jikwon_no,jikwon_name,buser_num,jikwon_pay,jikwon_jik
            from jikwon
            inner join buser on jikwon.buser_num=buser.buser_no
            where buser_name='{0}'
        """.format(buser_info)
        #print(sql)
        
        cursor.execute(sql)
        datas=cursor.fetchall()
        #print(datas,len(datas))
        
        if len(datas)==0:
            print(str(buser_info)+' 에 해당되는 자료는 없어요')
            return      # sys.exit(0) return대신 써도 됨
        
        for jikwon_no,jikwon_name,buser,jikwon_pay,jikwon_jik in datas:
            print(jikwon_no,jikwon_name,buser,jikwon_pay,jikwon_jik)
            
        print('인원수: {}'.format(len(datas)))
        
    except Exception as e:
        print('에러: '+e)
    
    finally:
        cursor.close()
        conn.close()
        
if __name__=='__main__':
    chulbal()
    