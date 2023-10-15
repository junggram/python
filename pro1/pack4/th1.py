# process : 실행 중인 프로그램을 의미함, 자신만의 메모리를 확보하고 공유하지 않음
# thread : light weight process라고도 함, 하나의 process내에는 한개의 thread가 존재함
# process 내에 여러 개의 thread를 운영하여 여러개의 작업을 동시에 하는 것처럼 느끼게 할 수 있다
# multi thread로 multi tasking이 가능 
# * 멀티스레드는 동시실행이 아님 돌아가면서 실행하는거임 *
import threading, time

def run(id):
    for i in range(1,101):
        print('id:{} --> {}'.format(id,i))
        time.sleep(0.3)
        
# thread 를 사용하지 않은 경우 run(1)의 작업이 끝날 때까지 run(2)는 하염없이 기다림
# run(1)
# run(2)

# thread 를 사용한 경우
# threading.Thread(target=수행함수명)
th1=threading.Thread(target=run, args=('일',)) # args 는 tuple type 이어야! 한다
th2=threading.Thread(target=run, args=('둘',))
th1.start()
th2.start()
th1.join()  # 사용자 정의 스레드(th1)가 종료할 때까지 메인스레드가 대기상태가 됨
th2.join()
print('메인스레드 프로그램 종료')