# Module : 소스 코드의 재사용을 가능하게 할 수 있으며, 소스코드를 하나의 이름 공간으로 구분하고 관리하게 된다
# 하나의 파일은 하나의 모듈이 된다
# 표준 모듈, 사용자 작성 모듈, 제3자(Third party) 모듈

# 모듈의 멤버 : 전역변수, 실행문, 함수, 클래스, 모듈

a=10
print(a)

def abc():
    print('abc는 모듈의 멤버 중 함수')
abc()

# 표준 모듈(내장된 모듈 읽기)
import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar # 월요일이 맨처음에 나오기때문에
calendar.setfirstweekday(6) # 일요일이 맨처음으로 나오도록 변경
calendar.prmonth(2022,10)

import os
print(os.getcwd())
print(os.listdir('/'))

print()
import random # import 모듈명 으로 모듈 읽기
print(random.random())
print(random.randint(1, 10))

from random import random # from 모듈명 import 멤버 를 적어도 사용 가능
print(random()) # random.random() 으로 안쓰고 바로 random()을 써도됨

from random import randint, randrange # 멤버를 여러개 한번에 import 해도됨
print(randint(1,10))

from random import * # 멤버들을 전부 로딩 *but 권장사항 아님, 메모리 낭비
