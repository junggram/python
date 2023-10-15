# 집합형 자료형 :  str, list, tuple, set, dict
# from Tools.demo.spreadsheet import colname2num

# list - 순서 O, 수정 O

a=[1,2,3]; b=[10,a,12.5,True,'문자열'] #변수를 붙여서 계속 쓰고싶으면 ; 을 붙이면됨
print(a,type(a),id(a))
print(b,type(b),id(b)) # list(b) 안에 list(a)가 들어가있음
aa=[]
bb=list()
print(type(aa), type(bb))

print('---'*20)

family=['엄마', '아빠', '나', '여동생']
print(family[2]) # 나 = 인덱싱
print(family[0:2]) # 엄마, 아빠 = 슬라이싱

family.append('남동생') # 맨뒤에 남동생 추가
family.insert(0, '할아버지') # insert(순서, 추가 할 data)
family.extend(['삼촌', '조카',]) # extend(집합형자료) 맨뒤에 자료 추가
family +=(['이모', '고모']) # 맨뒤에 자료 추가

family.remove('남동생') # data 제거
del family[2] # family[2]의 data 제거 

print(family, len(family))

print(family.index('나')) # '나' 의 순서 찾기

print('엄마'in family, '할머니'in family) #list 안에서 데이터의 유무 판별 (bool)

del family # 변수를 삭제
# print(family) 하면 오류가 난다 (변수를 지웠기 때문)

print('---'*20)

aa=[1,2,3,['a','kbs','c'],4,5] # 중첩 list 
print(aa)
print(aa[0])
print(aa[3])
print(aa[3][1]) # 중첩list 에서 원하는 data를 참조하고 싶을 때

print(id(aa))
aa[0]=333 # 요소값 수정해도 id가 변하지 않음
print(aa, id(aa))

print('---'*20)
aa2=['123', '34', '234']
print(aa2)
aa2.sort() # 사전식으로 정렬 (오름차순)
print(aa2)
aa2.sort(key=int, reverse=True) # 숫자처럼 취급(key=int)하고 내림차순 정렬(reverse=True)
print(aa2)

print('---'*20)
name=['소현', '현성', '다정']
print(name)
name2=name  # 얕은 복사 : 주소(id) 치환 
print(id(name), id(name2))

import copy #깊은 복사를 할 땐 import가 필요함
name3=copy.deepcopy(name) #깊은 복사. 새로운 객체로 생성 (같은 내용을 복사하더라도 id가 다름)

print(id(name), id(name2), id(name3))
name[0] = '용환'
print(name)
print(name2)
print(name3)

# 참고 사항 stack (세로형 통)과 queue(가로형 통)의 차이점
print('---'*5+"stack : LiFo, queue : FiFo"+'---'*5)
print('---'*5+"LiFo : Last in First out, FiFo : First in First out"+'---'*5)
sbs=[1,2,3]
sbs.append(4)
print(sbs)
sbs.pop() # 마지막 data 부터 한개씩 빠져나감
print(sbs)
sbs.pop()
print(sbs)
