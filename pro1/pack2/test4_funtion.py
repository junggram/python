# 함수 : argument 와 parameter 키워드로 matching 하기
# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 인수와 매개변수를 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start,end=5): # 위치 매개변수 , parameter(매개변수)에 초기값을 줄수도있다
    for dan in range(start, end+1):
        print(str(dan)+'단 출력')

showGugu(2,3) 
print()
showGugu(3) # 기본값 매개변수 : 매개변수가 없는데도 오류가 안나고 초기값을 사용하고있는 모습
print()
showGugu(start=2, end=3) # 키워드 매개변수
print()
showGugu(end=3,start=2) # 키워드 매개변수 = 순서가 바뀌어도 키워드가 같기 때문에 정상작동
print()
showGugu(2, end=3) # ???????
print()
# showGugu(start=2, 3) SyntaxError: positional argument follows keyword argument
# showGugu(end=3, 2) SyntaxError: positional argument follows keyword argument

print('\n가변인수 처리')
def func1(*ar): #packing 연산자 * 을 이용해서 여러개의 인자를 받을 수 있다
    #print(ar)
    for i in ar:
        print('밥: '+i )
    print()

func1('비빔밥','공기밥')
func1('비빔밥','공기밥','김밥')

def func2(a,*ar): #packing 연산자 * 을 이용해서 여러개의 인자를 받을 수 있다
# def func2(*ar,a): # 이렇게 사용하면 에러남 packing 연산자는 꼭 뒤에 있어야함
    print(a)
    for i in ar:
        print('밥: '+i )
    print()
    
func2('비빔밥','공기밥')
func2('비빔밥','공기밥','김밥')


print()
def calcProcess(op,*ar):
    if op=='sum':
        re=0
        for i in ar:
            re+=i
    elif op=='mul':
        re=1
        for i in ar:
            re*=i
    return re

print(calcProcess('sum', 1,2,3,4,5)) # 집합형 자료 ex) tuple (1,2,3,4,5) 는 안받아줌
print(calcProcess('mul', 1,2,3,4,5))

print()
def func3(w,h,**other): # DB연동할 때 많이 사용할 것임
    print('w:{}, h:{}'.format(w,h))
    print(other)
    
func3(55,160)
func3(55,160,irum='홍시 맛이 나서 홍시라') # dict type으로 입력됨
# func3(55,160,{'irum':'홍시 맛이 나서 홍시라'})   dict를 직접 넣으면 에러남
func3(55,160,irum='홍시 맛이 나서 홍시라',nai=232)

print()
def func4(a,b,*c,**d):
    print(a,b)
    print(c)
    print(d)

func4(1,2)
func4(1,2,3)
func4(1,2,3,4,5)
func4(1,2,3,4,5, x=6,y=7)