# class의 상속

class Person:
    say='난 사람~'
    nai='22'
    __kbs = '공영방송'  # private 멤버 변수 : __XXX 
    def __init__(self,nai):
        print('Person 생성자')
        self.nai=nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai,self.say))
    
    def hello(self):
        print('안녕',self.__kbs)
        
print(Person.say,Person.nai)
# Person.printInfo() 에러 : prototype의 메소드를 그대로 가져다 쓸 수 없음
p=Person('498')
p.printInfo()
p.hello()

print('---'*5+'Employee'+'---'*5)
'''
class Employee(Person):
    pass
        
emp=Employee('26') # Employee의 생성자가 없어도 부모생성자인 Person의 생성자를 불러와서 에러가 안남 
emp.printInfo()
'''
class Employee(Person):
    say='일하는 동물'
    subject='근로자'
    def __init__(self):
        print('Employee의 생성자')
        
    def printInfo(self):
        print('Employee의 printInfo 메소드') # 메소드 override (부모의 메소드를 재정의)
        
    def empPrintInfo(self):
        print(self.say, self.nai) # 자식class의 필드(say)와, 부모class의 필드(nai)를 불러옴
        print(self.say, super().say)# 자식class의 필드(say)와, 부모class의 필드(say)를 불러옴
        
        print(self.subject) # 자식class의 필드를 불러옴(subject) : 부모class에는 없는 자식 class의 고유필드
        
        self.printInfo() # 자식(본인)class의 메소드를 불러옴
        super().printInfo() # 부모class의 메소드를 불러옴
        self.hello() # 자식class에 hello메소드가 없기 때문에 부모class의 hello메소드를 불러옴
        
        # print(super.__kbs) # __kbs는 private 멤버변수이기 때문에 직접 부를 수 없다
                             # super.hello() 메소드를 통해서 불러야함
emp=Employee() # Employee의 생성자가 있을때 ( ) 안에 '나이' 를 넣으면 에러남
emp.printInfo() 
emp.empPrintInfo()

print('---'*5+'Worker'+'---'*5)

class Worker(Person):
    def __init__(self,nai):
        print('Worker 생성자')
        super().__init__(nai) # 부모 생성자를 호출
        
    def wPrintInfo(self):
        self.printInfo()
        
wor=Worker('287')
print(wor.say,wor.nai)
wor.wPrintInfo()

print('---'*5+'Programmer'+'---'*5)
class Programmer(Worker):
    def __init__(self,nai):
        print('Programmer 생성자')
        # super().__init__(nai)  # Bound call
        Worker.__init__(self, nai) # Unbound Call
        
    def ProShow(self):
        self.printInfo()
        
pr=Programmer('30')
print(pr.say, pr.nai)
pr.ProShow()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(type(3))
print(type(pr))
print(type(wor))
print(Programmer.__bases__, Worker.__bases__, Person.__bases__) # 최상위 부모(Person)의 부모는(object) = 모든 클래스의 최상위 부모는 'object'

