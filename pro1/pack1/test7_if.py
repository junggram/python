# 조건 판단문 if
# if 조건:실행문 elif 조건 ~ else: ~

var=1

# 파이썬의 if 조건문은 ( ) 가 없음, { } 대신 : 을 찍음

if var >= 3 :
    print('크구나') # 들여쓰기 있는지 꼭 확인
    print('참일 때') # 다음 실행문도 위와 들여쓰기가 맞아야함
    # pass 
else : 
    print('거짓일 때') 
    
print('end1')

print()
money=10000
age=23

if money >= 500:
    item='사과'
    if age <= 30:
        msg='청춘이다'
    else:
        msg='올드하다'
else:
    item='포도'
    if age >= 30:
        msg='성인이다'
    else:
        msg='애다'

print(item, msg)

print()
jumsu=85

if jumsu >=90:
    print('우수')
else:
    if jumsu >= 70:
        print('보통')
    else:
        print('저조')
        
print()
if jumsu >= 90:
    print('우수')
elif jumsu >=70:
    print('보통')
else:
    print('저조')

print()

print(int('5')+5) # 문자 '5'를 숫자 5로 캐스팅
print(str(5)+'5') # 숫자 5를 문자 '5'로 캐스팅

# jum=input('점수 입력:') #콘솔창에 입력해서 나오는 값은 str이다
# print(jum, type(jum))

# jum=int(input('점수 입력:')) #형변환을 해줌 int로
# print(jum, type(jum))
jum=80 #임시값
# if jum >= 90 and jum <=100: 을 줄여서
if 90 <= jum <= 100:
    grade='우수'
elif 70 <= jum <90:
    grade='보통'
else :
    grade='저조' 
print(grade)

print()
names=['홍길동', '신기해', '이기자']
if '홍길동' in names:
    print('친구 이름')
else:
    print('니 내 눈지 아니?')
    
if '홍길동' not in names: # 부정적인 조건을 주면 programming에선 속도에서 불리함
    print('친구 이름')
else:
    print('니 내 눈지 아니?')
    
print()
a='kbs'
b=9 if a == 'kbs' else 11 # if 문을 요약할 수 있다
print(b)

a=11
b='mbc' if a==9 else 'kbs'
print(b)

print()
a=8
if a<5:
    print(0)
elif a<10:
    print(1)
else:
    print(2)

print(0 if a<5 else 1 if a<10 else 2) #위를 한줄로 요약한 if 조건문

print(a*2 if a>5 else a+2)

print((a+2, a*2)[a>5]) # tuple로 사용할 수도 있다 [ ]안의 조건이 false 이면 '0'번째 방이 실행, true이면 '1'번째 방이 실행

