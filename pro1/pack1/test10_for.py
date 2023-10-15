#반복문 for

# for 변수 in 집합형자료: 실행문...

# for i in [1,2,3,4,5]:  list
# for i in (1,2,3,4,5):  tuple
for i in {1,2,3,4,5}:  # set
    print(i,end=' ')
    
print()
soft={'java':'웹언어', 'python':'만능언어', 'MariaDB':'데이터처리'}
print(soft.items()) # dict_items([('java', '웹언어'), ('python', '만능언어'), ('MariaDB', '데이터처리')])

for i in soft.items(): # list에 있는 아이템을 tuple 형식으로 
    print(i[0]+' : '+i[1])
    
print()
for k in soft.keys(): # 키 값만
    print(k, end=' ')
print() 
for k in soft.values(): # value 값만
    print(k, end=' ')

print()
li=['a','b','c']
for d in li:
    print(d)

 # 설명 enumerate
for idx, data in enumerate(li): # enumerate(li) 집합형 자료의 index와 data를 출력을 하는 내장함수 
    print(idx, data)

print('\n평균, 분산, 표준편차 구하기')

jum = [6,5,4,7,3]  
print(jum)
tot=0
for i in jum:
    tot+=i
avg=tot/len(jum)
print('mean: ', avg)  # 평균 구하기
    
tot=0
for i in jum:
    tot+=(i-avg) **2 #(i-avg) = 편차
var=tot/len(jum)
print('var: ',var) # 분산 구하기 = 편차 제곱합의 평균

import math
print('std: ', math.sqrt(var)) # 표준편차 구하기
print('std: ', var **0.5)  # 표준편차 구하기

print('---'*20)
for n in [2,3]:
    print('---{}단---'.format(n))
    for i in {1,2,3,4,5,6,7,8,9}:
        print('{}*{}={}'.format(n,i,n*i),end=' ')
    print()

print()
datas=[1,2,3,4,5]
for i in datas:
    if i==3 : continue
    if i==4 : break
    print(i,end=' ')
else:
    print('정상 종료일 때 수행')

print()
jumsu=[95,70,60,50,100]
number=0
for jum in jumsu:
    number +=1
    if jum < 70:continue
    print('%d번째 수험생은 합격'%number)

print()
li1=[3,4,5]
li2=[0.5,1,2]
result=[]

for a in li1:
    for b in li2:
        #print(a+b, end=' ')
        result.append(a+b)
print(result)

datas=[a+b for a in li1 for b in li2]
print(datas)

print('\n다량의 문자열 데이터 중 단어 수 출력')
import re
ss= '''
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
보건복지부 퇴직 공무원 70% 이상이 병원에 재취업한 것으로 드러나면서 전관예우 관행에 대한 비판이 커지고 있다.
5일 국회 보건복지위원회 여당 간사인 강기윤 의원이 복지부로부터 제출받은 ‘최근 3년간(2019년~2022년 8월) 퇴직자 재취업 현황’ 자료에 따르면, 퇴직자 24명 중 17명이 병원에, 3명은 법무법인에 재취업한 것으로 밝혀졌다.
퇴직 공무원이 퇴직일로부터 3년 이내에 취업대상 기관에 취업하기 위해서는 공직자윤리법 제17조와 제18조에 따라 관할 공직자윤리위원회의 취업심사를 받아야 한다.
3년간 퇴직한 24명 전원은 공직자윤리위원회에서 취업 가능 판정을 받은 것으로 나타났다.
'''

print(ss)
ss2=re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3=ss2.split(' ')
print(ss3)

cou={} # 단어의 발생횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i]+=1
    else:
        cou[i]=1
print(cou)

print()
for test_str in['111-1234','일이삼-사오육칠','222-1234']:
    if re.match(r'^\d{3,4}-\d{4}$',test_str):
        print(test_str, '전화번호 맞아요')
    else:
        print(test_str, '마! 제대로 확인하구로')

# 설명 price[f]
print('사전형 자료로 과일값 출력')
price={'사과':2000, '감':500, '배':1000}
guest={'사과':2, '감':3}
bill=sum(price[f]*guest[f] for f in guest)
print('호갱이 구매한 과일 총액 : {}원'.format(bill))

print()
temp=[1,2,3]
for i in temp:
    print(i,end=' ')
print()
print([i for i in temp])
print({i for i in temp})

temp2=list()
for i in temp:
    temp2.append(i+10)    
print(temp2)
temp2=[i+10 for i in temp]
print(temp2)

# 설명 i*i
print()
datas=[1,2,'a',True,3]
li=[i*i for i in datas if type(i)==int]
print(li)

# 중복된값은 전부 제거되기 때문에 １,２,３만 남음
print()
datas={1,1,2,2,2,3}
se={i*i for i in datas}
print(se)

# value : key 로 변경하면서 순서를 바꿔줌
print()
id_name={1:'tom',2:'james'}
name_id = {value:key for key, value in id_name.items()}
print(name_id)

