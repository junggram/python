#반복문 continue, break

a=0

while a<10:
    a+=1
    if a==3:continue # continue를 만나면 아래를 수행하지않고 다시 while문 처음으로 돌아감 
    if a==5:break # break를 만나면 바로 반복문 수행 종료
    print(a)
else:
    print('while문 정상 수행')
    
print('while 수행 후 %d'%a)

print('---'*20)
# 난수 발생
import random
#random.seed(42)
num=random.randint(1, 10)
#print(num)
'''while True:
    print('1~10 사이의 컴이 가진 예상 숫자 입력')
    guess = int(input())
    if guess==num:
        print('성공'*10)
        break
    elif guess <num:
        print('더 큰 수 입력')
    elif guess > num:
        print('더 작은 수 입력')'''
        
# 의사 난수(pseudo random)        
friend = ['tom', 'john', 'oscar']
print(friend)
print(random.choice(friend)) # 한개만
print(random.sample(friend,2)) # 입력한 숫자만큼
random.shuffle(friend) # 모델의 data들의 순서를 섞음
print(friend)