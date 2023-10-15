'''
여러줄 주석
파이썬은 ' 과 " 를 구별하지 않는다
'''

"""
여러줄 주석
"""

'''# 한줄 주석 (범위 지정 후 ctrl + / 하면 주석처리됨)

#변수 선언 시 type을 선언하지 않습니다 (java와의 차이점)
var1='안녕'
var1=5
print(var1)


print()
a=10
#들여쓰기 하면 안됨 줄을 잘 맞춰야함
b=12.5 
c=b
print(a, ' ', b, ' ', c)

#파이썬은 참조데이터만 있기 때문에 b와 c의 값이 같게나옴
print('주소출력: ', id(a), ' ', id(b), ' ', id(c)) 

#주소 비교, 값 비교
print(a is b, a==b) 
print(c is b, c==b)

aa=[1000]
bb=[1000]
print(aa == bb, aa is bb) 
print(id(aa), ' ', id(bb))

print('--------------------ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
A=1; a=2;

#변수는 대소문자 구분함
print('A+a', A+a, id(A), id(a)) 

print()
import keyword

#키워드는 변수명으로 사용할 수 없음 (숫자로 시작해도 안됨)
print('키워드(예약어) 목록: ', keyword.kwlist)

print()
#   10진수,  8진수,   16진수,   2진수
print(10, oct(10), hex(10), bin(10))
# 반대로 번역도 가능함
print(10, 0o12, 0xa, 0b1010)

print('자료형')
print(3, type(3)) #int
print(3.4, type(3.4)) #float
print(3+4j, type(3+4j)) #complex (실수 + 허수)
print(True, type(True)) #bool


#집합형 참조데이터
print('good', type('good')) #str
print((1,), type((1,))) #튜플 tuple
print([1], type([1])) #리스트 list
print({1}, type({1})) #셋 set
print({'k':1}, type({'k':1})) #딕셔너리 dict

# type 을 확인하는 연산자 리턴type bool
print(isinstance(1.2, int)) 
print(isinstance(1.2, float))'''

'''import random

c=int(input())
print(c)
for test in range(c):
    n=random.randint(1, 10)
    print(n,end=' ')
    for i in range(n):
        jumsu=random.randint(1,100)
        print(jumsu,end=' ')
    print()  '''
        
c=int(input())
for i in range(c): 
    jumsu=list(map(int,input().split()))
    n=jumsu[0]
    avg=sum(jumsu[1:])/n
    cnt=0
    
    for i in jumsu:
        if i>avg:
            cnt+=1
    result=(cnt/jumsu[0])*100
    print(f'{result:.3f}'+'%')
    

    