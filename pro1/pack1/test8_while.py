# 반복문 while
# while 조건: ~
# from conda.common._logic import FALSE

# a=1
# while a<=5:
#     print(a,end=' ')
#     a += 1  # 파이썬엔 a++ 증감연사자는 없음 
    
# print('while 수행 후 %d'%a)

# print()
# i=1  # 중복 while문
# while i <= 3:
#     j=1
#     while j<=4:
#         print('i:'+str(i)+',j:'+str(j))
#         j=j+1
#     i+=1

# print('1~100사이의 정수 중 3의 배수의 합 출력')
# i=1; hap=0 # while 안에 if 조건문도 가능
# while i < 100:
#     if i%3==0:
#         hap += i
#     i+=1
#     # print(i, end=' ')
# print('합은{}'.format(hap))

# print()
# colors=['r','g','b']
# print(colors[0])
# a=0
# while a<len(colors):
#     print(colors[a], end=' ')
#     a+=1
    
# print()

# while colors:
#     print(colors.pop(0), end=' ') # pop() 이면 stack 형식으로 b,g,r로 출력됨
#     #print (len(colors))
    
# print()
# i=1
# while i<=10:
#     j=1
#     re = ''
#     while j<=i:
#         re=re+'*'
#         j+=1
#     print(re)
#     i+=1

# print('-----'*10)
# import time # 자바에서 thread 처럼 텀을 둘 때 사용
# # time.sleep(3)

# print('end')

# sw=input('폭탄 스위치를 누를까요?[y/n]')
# if sw=='Y' or sw=='y':
#     count=5
#     while 1<=count:
#         print('%d 초 남았습니다'%count)
#         time.sleep(1)
#         count-=1
#     print('폭발')
# elif sw=='N' or sw=='n':
#     print('작업 취소')
# else:
#     print('y 또는 n을 눌러주세요')
    

# #문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력

# i=1
# hap = 0
# while i < 100 :
#     if i%3 == 0 and i%2 != 0:
#         hap += i
#         print(i, end=' ')
#     i+=1
# print("총 합계는", hap)

#문2) 2 ~ 5 까지의 구구단 출력

# i=2  # 중복 while문
# while i <= 5:
#     print(str(i)+'단')
#     j=1
#     while j<=9:
#         # print('i:'+str(i)+',j:'+str(j))
#         # print(int(i)+'*'+int(j)+'='+int(i)*int(j))
#         print(str(i) + 'x' + str(j) + '=',i*j)
#         j=j+1
#     i+=1


# #문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력

# i = -1
# datalist = []
# while i < 99 :
#     i = i + 2
#     datalist.append(i)
# print(len(datalist))

# j = 0
# while j < len(datalist): 
#     if j % 2 == 0 :
#         datalist[j] = datalist[j]*-1
#         # print('j%2 = ',datalist[j])
#     else :
#         datalist[j] = datalist[j]
#         # print('j%2 != ',datalist[j])
#     j = j+1
# print(sum(datalist))

# #문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력

i = 2
j = 1
a = []
while i <= 10 :
    if i % j == 0 :
        print(i,'%',j)
        a.append(i)
        print(a)
        j = j + 1
        print('j = ',j)
    i = i +1
print('i = ',i)
    













































# #문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
# print('---1번---')
# sum=0
# while i <100:
#     if i%3==0 and i%2!=0:
#         sum+=i
#     i+=1
# print(sum)


# #문2) 2 ~ 5 까지의 구구단 출력
# print('---2번---')
# g=2
# while g<6:
#     m=1
#     while m<10:
#         print(g,'*',m,'=',g*m,end=' ')
#         m+=1
#     g+=1
# print()
# #문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
# print('---3번---')
# i=1
# cnt=1
# tot=0
# while i<100:
#     if cnt%2==0: #짝수 위치 숫자 처리
#         tot+=i
#         print(i,end=' ')
#     else: #홀수 위치 숫자 처리
#         k=i*-1 #부호 변경
#         tot+=k
#         print(k,end=' ')
#     cnt +=1
#     i+=2 #증가치 2
# print('\ntot:', tot)

# #문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
# print('---4번---')
# aa=2
# count=0

# while aa <= 1000:
#     imsi=False
#     bb=2;
    
#     while bb<=aa-1: # 3부터 약수를 걸러내기위한 코딩         #bb==3 일때 3<=3-1 여기도 False가 되기때문에
#         if aa%bb==0: # aa==3, bb==2 라고 가정하면 False                       ㅣ 
#             imsi=True # 수행되지않고                                          ㅣ while 문을 빠져나가서
#         bb+=1 # 빠져나가서 다시 while 문을 돌지만                                ㅣ
#     #                                                                      ㅣ
#     if imsi==False: # 이쪽으로 들어왔고 맨처음 imsi를 False로 정의해놓은게 있으니 True가 됨
#         print(aa,end=' ') # 조건이 True이니까 이쪽이 수행되고
#         count +=1 # count도 1만큼 중첩
#     aa+=1 # 빠져나와서 aa도 1만큼 중첩  다시  while aa <= 1000: 여기부터 시작
    
# print('\ncount: ', count)

# a=2
# b=[]
# while 1<a<1000:
#     if a==2 or a==3 or a==5 or a==7 or a==11 or a==13 or a==17 or a==19 or a==23 or a==29 or a==31:
#         b.append(a)
#     elif a!=1 and a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0 and a%11!=0 and a%13!=0 and a%17!=0 and a%19!=0 and a%23!=0 and a%29!=0 and a%31!=0:
#         b.append(a)
#     a+=1
# print(b,len(b))