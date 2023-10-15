# 집합형 자료형 :  str, list, tuple, set, dict

# tuple - list와 유사하나 읽기 전용임 순서O, 수정X (읽기전용이기 때문에 list보다 속도가 빠름)
t=('a','b','c','a')
t='a','b','c','a' # ( ) 생략 가능하지만 가독성을 위해 ( ) 를 권장
print(t,type(t),len(t),t.count('a'),t.index('b'))

print(t[0])
#t[0]='k'  # TypeError 발생 tuple은 수정이 불가하다

imsi = list(t) # 형 변환 (tuple => list)
print(imsi)
imsi[0]='k' # 형 변환 후 data 값 변경
t=tuple(imsi) # 다시 형 변환 (list => tuple)
print(t)

print()
print((1), type((1))) # type 이 int
print((1,), type((1,))) # type 이 tuple

print()
t1=(10,20)
a,b=t1
b,a = a,b
t2=a,b
print(t2)

print('---'*20)
# set - 순서X, 중복X
a={1,2,3,1}
print(a,type(a),len(a)) #{1,2,3} 만 나옴 중복이 안되기 때문에 길이도 3임
b={3,4}

print(a.union(b)) # 합집합
print(a|b)        # 합집합
print(a.intersection(b)) # 교집합
print(a&b)               # 교집합
print(a-b) # 차집합

print()
print(a)
# print(a[0]) 
# a[0]=100 # 순서가 없기 때문에 '0번째'에 값을 줄 수 가 없다 = Error

a.update({4.5}) # update함수를 이용한 추가 가능
a.update([6,7,8]) # list와
a.update((9,)) # tuple을 이용해서 추가 가능
print(a)

a.discard(3) # 값 삭제
#a.remove(5) # 값 삭제
# a.discard(3) # 값 삭제 , 3이 있으면 삭제 없어도 에러 안남
# a.remove(5) # 값 삭제 , 5가 있으면 삭제 없으면 에러 남
print(a)

c=set()
c=a
print(c)
a.clear() # data 삭제
print(a)
print(c)

print()
li=[1,2,3,1,2,3]
print(li)
imsi=set(li) # 형변환 ( list => set )
li=list(imsi)
print(li)

print('---'*20)
# dict {'key' : 'value'} - 순서X, key를 이용해 value를 참조

my=dict(k1=1, k2='mbc', k3=3.4)
print(my, type(my))
your={"k1":1, "k2":'mbc', "k3":3.4, "k4":[60,70,80]} # list,  tuple도 value로 사용가능
print(your, type(your),len(your))
print(your["k4"]) # key값으로 value값을 참조 가능 (인덱싱 불가)

your['k5']='오라클' #key, value로 추가
print(your)
del your['k5'] # key값으로 삭제
your.pop('k1') # key값으로 삭제
print(your)

your['k2']='김구라' # key값으로 수정 가능
print(your)

print(your.keys()) # key값만 보기
print(your.values()) # value값만 보기
print('k3'in your) # key값으로 value의 유무 확인
print('--1번--')
li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2] # 리스트 타입
im = set(li)
li = list(im)
print(li)

print('--2번--')
for i in {1, 2, 3, 4, 5, 5, 5, 5}:
  print(i, end = ' ')
print()
print('--5번--')
i = 0
while True:
    if i%10!=3:
        i += 1
        continue       
               
    if i > 100: break 
                 
    print(i, end=' ')
    i += 1