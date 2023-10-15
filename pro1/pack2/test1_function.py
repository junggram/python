# function(함수) 
# 여러 개의 수행문을 하나의 이름으로 묶은 실행단위(unit)
# 반복 소스의 재활용(단순화)
# 디버깅이 쉽다. 유지 보수비가 적다.
# 내장함수, 사용자 정의 함수

# 내장함수 : maker가 제공
a=3
print(a)
print(sum([3,5]))
print(bin(8))
print(int(1.6),float(3))

a=10
b=eval('a+5') #문자열에 a값을 대입 eval()
print(b)


#...
print(round(1.2), round(1.6)) # 반올림
import math
print(math.ceil(1.2),math.ceil(1.6)) # 정수 근사치 중 큰수
print(math.floor(1.2),math.floor(1.6)) # 정수 근사치 중 작은수

print()
b_list=[True,1,False]
print(all(b_list)) # 모든 값이 참이면 참
print(any(b_list)) # 하나라도 참이면 참

b_list=[1,3,2,5,7,16]
print(all(a<10 for a in b_list))
print(any(a<10 for a in b_list))

# 이해안됨
print()
x=[10,20,30]
y=['a','b']
for i in zip(x,y): # 인자로 가진 변수들의 data를 커플링 = (10, 'a'),(20, 'b')
    print(i)
    