# class : 새로운 타입을 생성, 객체 지향적(중심적)인 프로그래밍 = 장점1. 자원의 재활용, 장점2. 이벤트처리 가능
# 형식 class 클래스명( ): 멤버(필드, 메소드) ~
# 생성자, 소멸자가 있다
# 접근지정자 없다 (ex public, private 등등 기본적으로 전부 public), 메소드 오버로딩 없다
# 다중상속 가능, interface 없다

print('뭔가를 하다가 모듈의 멤버인 클래스를 선언하기')

class TestClass: # prototype (원형클래스). 고유의 이름 공간을 확보
    aa=1 # 멤버 변수(멤버 필드), public
    
    def __init__(self): # 생성자
        print('생성자')
        
    def __del__(self): # 소멸자
        print('소멸자')
        
    def printMessage(self): # 메소드  반드시 self를 가져야함
        name='한국인' # 지역변수
        print(name)
        print(self.aa) # self = 자바의 this
        
print(TestClass, id(TestClass)) # interpreter 가 훑고가면 class가 객체로 만들어짐
print(TestClass.aa) # 자바에서 객체에 .을 찍고 안에 요소를 사용할 수 있는 것처럼 사용 가능

print()
test=TestClass() # 생성자 호출한 후 TestClass type의 객체를 생성
print(test.aa)

# TestClass.printMessage() 오류남 원형클래스의 이름으로는 prototype 메소드를실행할 수 없다
test.printMessage()  # Bound method call   * 실행시에 TestClass() type의 test라는 변수이름이 (  ) 안에 들어간다
print()
TestClass.printMessage(test) # UnBound method call * 직접 (  ) 안에 넣어줘야함

print()
print(type(1))
print(type(1.1))
print(type(test))
print(id(test),id(TestClass))