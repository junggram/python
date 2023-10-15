# GIL 정책에 의해 완전한 스레드 구현은 불가하다
# 그래서 mutiprocessing 모듈로 GIL 정책을 우회하여 병렬처리 가능하도록 하고있다

from multiprocessing import Pool, Process
import time
import os

# Pool : 입력값에 대해 process들을 건너건너 분배하여 함수 실행을 병렬처리

def func(x):
    print('값',x,'에 대한 작업 process id: ',os.getpid())
    time.sleep(1)
    return x * x

print('\n----------------')
def func2():
    print('연속적으로 어떤 작업을 진행')
    time.sleep(1)
    
def doubler(num):
    result=num+10
    func2()
    proc=os.getpid()
    print('num:{0}, result:{1}, process id:{2}'.format(num, result, proc))

if __name__=='__main__':
    startTime=int(time.time())
    
    ''' 직렬 처리
    for i in range(0,10):
        print(func(i))
    '''
    
    #병렬 처리
    p=Pool(processes=3)   # processess를 늘림 ( 3~5개가 적당 )
    print(p.map(func,range(0,10)))
    
    
    endTime= int(time.time())
    print('총 작업 시간: ', (endTime-startTime))
    
    print('---'*20)
    numbers=[1,2,3,4,5]
    procs=[]
    
    for idx, number in enumerate(numbers):
        proc=Process(target=doubler, args=(number,))
        procs.append(proc)  #process에 join()을 추가할 의도
        proc.start()
        
    for proc in procs:
        proc.join()
    
    