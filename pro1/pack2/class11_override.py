# 메소드 override(재정의)

# 추상클래스 (interface)는 반드시 메소드를 override를 해줘야한다
# 하지만 기본적으로 파이썬은 추상클래스를 지원하지 않는다

class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self):
        print('Child1에서 override함')  # 메소드 override 

c1=Child1()
c1.printData()

class Child2(Parent):
    def printData(self):
        print('Child2에서 override함')  # 메소드 override 
        print('override는 부모의 메소드를 자식이 재정의 한 것')
    
    def abc(self):
        print('Child2 고유 메소드')
c2=Child2()
c2.printData()

print('---- 다형성 ----') 
par=Parent()
par=c1 # 부모객체의 변수에 자식의 주소를 치환할 수 있다
par.printData() # 치환 후 자식의 메소드(override 된 메소드)를 호출할 수 있다
print()
par=c2
par.printData()
par.abc() # Java에선 자식 객체의 고유메소드를 불러올 수 없지만 파이썬에서는 가능하다

print()
plist=[c1,c2]
for i in plist:
    i.printData()