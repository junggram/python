# for + range
print(list(range(1,6))) # 1'이상' 6'미만
print(list(range(1,6,2))) # 1'이상' 6'미만 등차 2
print(list(range(6))) # '0' 이상 6'미만'   =    list의 방번호는 '0' 부터
print(set(range(1,6)))
print(tuple(range(1,6)))

print()
for i in range(6):
    print(i,end=' ')
print()
for _ in range(6):
    print('안녕',end=' ')
print()

print()
for i in range(1,10):
    print('{0}*{1}={2}'.format(2,i,2*i), end=' ')
    
print()
tot=0
for i in range(1,11):
    tot+= i
print('합은: '+str(tot))
print('합은:',sum(range(1,11))) # 위 합을 구하는 코드를 sum함수로 대체


# 문1) 2~9단까지 출력
li1 = [2,3,4,5,6,7,8,9]
li2 = [1,2,3,4,5,6,7,8,9]
result = []
for a in li1:
    print(a, '단')
    for b in li2:
        print(str(a)+'x'+str(b)+' = ', a*b)
        result.append(a*b)
    
    

# 문2) 1~100 사이의 3의 배수이면서 5의 배수의 합 출력


# 문3) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 두 수 출력















































# 문1) 2~9단까지 출력
for i in range(2,10):
    print('---{}단---'.format(i))
    for u in range(1,10):
        print('{0}*{1}={2}'.format(i,u,i*u), end=' ')
    print()

# 문2) 1~100 사이의 3의 배수이면서 5의 배수의 합 출력
sum=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        sum=sum+i
print(sum)
# 문3) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 두 수 출력
#출력 예) 1 3
#        2 2
for d1 in range(1,7):
    for d2 in range(1,7):
        if (d1+d2)%4==0:
            print(d1,d2)
        else:
            pass
        
print()
# n-gram : 문자열에서 N개의 연속된 요소를 추출하는 방법
text='hello'
for i in range(len(text)-1):
    print(text[i:i+2])