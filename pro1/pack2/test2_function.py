# 함수 만들기
# def 함수명(매개변수,...):~

print('뭔가를 하다가...')

def DoFunc1():  # 함수의 생성
    print('DoFunc1 수행')
    # return None 이 생략되어있다
    
print('뭔가를 하다가2...')
DoFunc1()  #함수의 호출
print('뭔가를 하다가2...')
DoFunc1()  #함수의 호출
print(DoFunc1)
## 설명
DoFunc2=DoFunc1 # 주소를 치환
DoFunc2()
print(DoFunc1()) # None

print()
def DoFunc3(para1, para2): # 매개 인자를 넣어줌
    # pass를 쓸수도있음
    result=para1+para2
    # print(result)
    return result

print(DoFunc3(10,20))
aa=DoFunc3(10,20)
print(aa)
print(id(DoFunc3), DoFunc3, DoFunc3(1,2))
print('현재 파일(모듈)이 사용 중인 객체 목록: ',globals()) # 현재 파일(모듈)이 사용 중인 객체 목록 확인 방법

print(DoFunc3('대한','민국'))
# print(DoFunc3('대한',1))  =>  에러  * 인자끼리의 data type이 맞아야함
# print(DoFunc3(1)) => 에러 * 인자의 갯수를 정확히 입력해야함

print('-------------------')
def dofunc4(arg1,arg2):
    if(arg1+arg2)%2==1:
        return
    else:
        aa=dofunc5(arg1,arg2) # 함수 내에서 다른 함수 호출
        print(aa)

def dofunc5(arg1,arg2):
    return arg1+arg2

dofunc4(5,6)
dofunc4(4,6)

print()
def swapfunc(a,b):
    return b,a  # tuple type으로 묶여서 return 하지만 tuple에서 ( )가 생략된 모습  * 두개의 값을 리턴하는게 아님
    #return (b,a)
    #return [b,a]
a=10;b=20
print(swapfunc(a,b))

print()
def func1(): # 함수 안에서 함수를 정의
    print('func1 함수 멤버')
    def func2():
        print('func1의 내부 함수인 func2 멤버')
    func2() # 내부함수는 함수안에서 호출을 해줘야 응답함
    
func1()

print()
# if 조건식 안에 함수 사용
def isOdd(para):
    return para%2==1

print(isOdd(5))
print(isOdd(6))

mydict={x:x*x for x in range(11) if isOdd(x)}
print(mydict)

print('함수 연습용 게임 ---')
import random
import time

def gameSijak():
    print('보물을 찾아 여행을 떠나자. 동굴 문은 두개다')
    print('동굴 속에는 착한 용과 무서운 용이 있다')
    print('랜덤하게 동굴을 선택해 착한 용을 만나면 보물을 획득, 나쁜 용을 만나면 황천길')

def chooseCave():
    cave=''
    while cave !='1' and cave !='2':
        print('동굴을 선택 (1 또는 2)')
        cave=input()
    return cave

def chkCave(selectNum):
    print('동굴에 도착')
    time.sleep(3)
    rndNum=random.randint(1, 2)
    
    if selectNum==str(rndNum):
        print('와우 착한용을 만나 보물을 획득 했습니다')
    else:
        print('와우 착한용을 만나 보물을 획득 했..... 을 줄 알았지만 사망')

playAgain = 'y'
while playAgain=='y':
    gameSijak()
    caveNumber = chooseCave()
    chkCave(caveNumber)
    print('계속할까요?(y or n)')
    playAgain=input()













