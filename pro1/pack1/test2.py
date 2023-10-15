'''#연산자, 출력 서식

v1=2 #치환
v1=v2=v3=v4=5
print(v1,v2,v3,v4)

v1=1,2,3
print(v1) #집합형 변수
v1, v2=10, 20
print(v1,v2)
v2,v1=v1,v2 #스와핑
print(v1,v2)

print('값 할당 packing')
# v1, *v2 = 1,2,3,4,5 => v1= 1, v2=[2, 3, 4, 5]
# *v1, v2 = 1,2,3,4,5 => v1= [1,2,3,4], v2=5
# *v1, *v2 = 1,2,3,4,5 => 오류남
print(v1)
print(v2)

v1, v2, *v3=1,2,3,4,5 # v1=1, v2=2, v3=[3,4,5]
# v1, *v2, *v3=1,2,3,4,5 => 오류남 
print(v1,v2,v3)

print()
print('--------------------------------------ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('\n연산자(산술, 관계, 논리)')
print(5+3, 5-3, 5*3, 5/3)
#      몫   나머지   몫+나머지
print(5//3, 5%3, divmod(5,3) )

# 연산순서 = 소괄호() > 산술연산자(**, *, /) > 산술연산자(+,-) > 관계연산자 > 논리연산자 > 치환(=)
print('연산자 우선순위', 3+4*5,(3+4)*5 )

print('관계연산자')
print(5>3, 5==3, 5!=3)
print('논리연산자')
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))

print('문자열 더하기 연산자')
print('파이썬'+'만'+'세')
print('파이썬'*20)

print('누적')
a=10
a=a+1
a+=1 # a++, ++a 같은 증감연산자는 파이썬에는 없음 
print('a:', a)

print()
print(a, a*-1, -a, --a) # 부호 바꾸는 연산도 가능 * --a 는 증감연산자가 아니다 *

print('bool:', True, False, type(True))
print(bool(True), bool(1), bool(-23.4), bool('kbs')) # 0이외의 값이 들어가있으면 True
print(bool(False), bool(0), bool(''), bool(None), bool([]), bool({}), bool(())) # 0이나 값이 없으면 False



print('***'*10) 
# 출력 서식
print(format(123.45678, '10.3f'))
print(format(123.45678, '10.3'))
print(format(123, '10d'))
print ('{0:.3f}'.format(1.0/3))
print ('{0:_^11}'.format('hello'))
# name, book 에 데이터 주입
print ('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# 파이썬도 index는 0부터 시작
print('이름:{0}, 가격:{1}'.format('마우스', 5000))
# 순서대로 대입되기때문에 index 부여 안해도됨
print('이름:{}, 가격:{}'.format('마우스', 5000))
print('이름:{1}, 가격:{0}'.format('마우스', 5000))
# 여러번 사용 가능
print('이름:{1}, 가격:{0}, 가격:{0} '.format('마우스', 5000))


print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))

print('~~~'*10)
print('aa\tbb') # \t 이스케이프 문자 (tab키)
print(r'aa\tbb') # r(raw string)이 선행문자로 오면 이스케이프 기능이 해제
print("c:\aa\abc\nbc.txt")
print(r"c:\aa\abc\nbc.txt")

print('aa', end=', ') # print()문은 기본적으로 실행 후 줄을 바꿈 end= 을 쓰면 줄바꿈을 안함
print('bb')'''

c = int(input())

for i in range(c):
    a = list(map(int,input().split()))
    n = a[0]
    del a[0] # 학생의 수 리스트에서 제거
    a.sort() # 오름차순으로 정렬
    avg = sum(a)/n

    for j in range(n):
        if a[j]>avg: # 평균보다 높은 경우
            print('%.3f%%' %((n-j)/n*100)) # 학생의 비율 출력
            break
        elif j==n-1: # 평균보다 높은 학생이 없는 경우
            print("0.000%")
