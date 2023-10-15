# 클로저(closure) : scope에 제약을 받지않는 변수를 포함하고 있는 코드 블록이다
# 내부함수의 주소를 반환함으로 해서 함수 내의 지역변수를 함수 밖에서 참조 가능

def funcTimes(a,b):
    c=a*b
    return c

print(funcTimes(2,3))

kbs = funcTimes(2,3)
print(kbs)
kbs=funcTimes
print(kbs)
print(kbs(2,3))
print(id(kbs),id(funcTimes))

del funcTimes
print(kbs(2,3))

mbc=sbs=kbs
print(mbc(2,3))
#-------------------------------------------
print('클로저를 사용하지 않은 경우 ---')
def out():
    count=0
    def inn():
        nonlocal count
        count+=1 # count 가 inn()의 지역변수로 선언된게 없어서 에러남 => nonlocal count를 해주면 out()의 지역변수를 참조
        return count
    # print(inn()) inn의 리턴값을 프린트해서 1을 리턴할수도있고
    imsi=inn()
    return imsi #변수에서 inn()을 호출해서 그 값을 리턴해도된다    
# print(out()) None 리턴
# print(count) 에러남
#out()
print(out())

print('\n클로저를 사용한 경우------')
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1 
        #...
        return count
    return inner # <== 클로저 : 내부함수의 주소를 반환
var1=outer()
print(var1)
print(var1())
print(var1())
print(var1())
print(var1())

print('*** 수량 * 단가 * 세금을 계산하는 함수 만들기')
#분기별로 세금은 동적이다
def outer2(tax): # tax는 지역변수임 (전역변수 x)
    def inner2(su, dan):
        amount=su*dan*tax
        return amount
    return inner2 # inner2() 하면 클로저가 아님 

# 1분기에는 tax 0.1
q1=outer2(0.1)
result1=q1(5,50000)
print('result1: ',result1)
result2=q1(1,10000)
print('result2: ',result2)

# 2분기에는 tax 0.05
q2=outer2(0.05)
result3=q2(5,50000)
print('result3: ',result3)