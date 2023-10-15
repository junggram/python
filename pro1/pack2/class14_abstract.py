# 추상클래스 = 자식클래스에서 부모 메소드 이름을 강요하기 위해서 사용

from abc import *

class AbstractClass(metaclass=ABCMeta): # 추상 클래스가 됨
    @abstractmethod
    def myMethod(self): # 추상 메소드가 됨
        pass
    
    def normalMethod(self):
        print('추상 클래스는 일반 메소드를 가질 수도 있다')
        
# parent=AbstractClass() # 추상 클래스는 변수에 담을 수 없다, Can't instantiate abstract class AbstractClass

class Child1(AbstractClass): # 추상 클래스를 상속 받았기 때문에
    name='난 Child1'
    
    def myMethod(self):
        print('Child1에서 추상메소드를 override 함') # 추상메소드를 override를 하지 않으면 호출할 수 없다
        
c1=Child1()
print(c1.name)
c1.myMethod()

print()
class Child2(AbstractClass):
    
    def myMethod(self):
        print('Child2에서 추성훈의 마법을 풀다')
        print('이제는 미녀에요')
    def normalMethod(self):
        print('추성훈 클래스의 일반 메소드는 orverride가 선택적이다')
        
    def good(self):
        print('Child2의 고유 메소드')
        
c2=Child2()
c2.myMethod()
c2.normalMethod()
c2.good()

print('---'*20)
imsi=c1
imsi.myMethod()
print()
imsi=c2
imsi.myMethod()