# thread를 사용한 디지털 시간 출력

import time

now=time.localtime()
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year,
                                       now.tm_mon,
                                       now.tm_mday,
                                       now.tm_hour,
                                       now.tm_min,
                                       now.tm_sec))
print('---'*20)

import threading

def cal_show():
    now=time.localtime()
    print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year,
                                       now.tm_mon,
                                       now.tm_mday,
                                       now.tm_hour,
                                       now.tm_min,
                                       now.tm_sec))
    
def my_run():
    while True:
        now2=time.localtime()
        if now2.tm_min==5: break
        cal_show()
        time.sleep(1)
    
th1=threading.Thread(target=my_run)
th1.start()

th1.join()
print('프로그램 종료')