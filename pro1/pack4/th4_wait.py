# 스레드간 자원 공유 + 스레드 활성화/비활성화

import threading, time

bread_plate=0 # 빵접시 - 공유자원
lock = threading.Condition()

class Maker(threading.Thread):      # 빵 생산자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()  # 공유자원 충돌 방지를위한 공유자원 점유
            while bread_plate>=10:
                print('빵 생산 초과로 대기')
                lock.wait()     # 스레드 비활성화  
            bread_plate+=1   
            print('빵 생산 : ', bread_plate)
            lock.notify()   # 스레드 활성화
            lock.release()  # 공유자원 점유 해제
            time.sleep(0.1)
            
class Consumer(threading.Thread):      # 빵 소비자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()  # 공유자원 점유
            while bread_plate <1:
                print('빵 재고 부족으로 대기')
                lock.wait() # 스레드 비활성화
            bread_plate-=1
            print('빵 재고 : ', bread_plate)
            lock.notify()   # 스레드 활성화
            lock.release()  # 공유자원 점유 해제
            time.sleep(0.11)
            
mak=[]; con=[]

for i in range(5):  # 생산자 수 5
    mak.append(Maker())


for i in range(5):  # 소비자 수 5
    con.append(Consumer())
    
for th1 in mak:
    th1.start()
    
for th2 in con:
    th2.start()
    
for th1 in mak:
    th1.join()
    
for th2 in con:
    th2.join()
    
print('오늘 영업 끝')