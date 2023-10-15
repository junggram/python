# 사용자 작성 모듈
print('뭔가를 하다가...')

# 다른 모듈의 멤버 호출
list1=[1,3]
list2=[2,4]

import pack2.mymodule1  # 호출방법 1 (1회성 호출을 할 것 같을 때)
pack2.mymodule1.listHap(list1,list2) #패키지명.모듈명.멤버 로 호출가능
print()

def abcd():
    if __name__=='__main__': # java와는 다르게 파이썬은 메인모듈 구분하기가 어렵다 (메인메소드처럼 구분하는게 없기 때문)
        print('난 메인 모듈이야') # 그렇기 때문에 메인모듈엔 명시를 해주는편이 좋음 (나중에 방법을 알려주겠음)

abcd()

print('가격은{}원'.format(pack2.mymodule1.price))

from pack2.mymodule1 import price  # 호출방법 2 (자주 쓸 거 같을때 )
print('가격은{}원'.format(price))

from pack2.mymodule1 import kbs, mbc
kbs()
mbc()

print('\n다른 패키지에 있는 모듈 읽기') # 다른패키지에 있는 모듈도 동일하게 호출할 수 있음 import or from

import etc.mymodule2
print(etc.mymodule2.Hap(5, 3))

from etc.mymodule2 import Cha
print(Cha(2, 1))

print('\n다른 패키지(path가 설정된)에 있는 모듈 읽기') # Window - preferrences - pyDev - interpreter - python interpreter - library 에 등록되어있는 경로 

import mymodule3  
print(mymodule3.Gop(5, 3))
from mymodule3 import Nanugi
print(Nanugi(5, 3))
