# 클래스의 이해

kor=100

def abc(): # 함수
    a=10   # 지역변수
    print('함수')
    
class MyClass:  # 클래스 ()는 상속할때만 쓴다
    kor=90      # 멤버변수
    
    # 생성자에 쓸 내용이 없으면 생략해도됨 ( interpreter가 기본생성자를 생성, java에서 기본생성자를 생략하는것과 같음 ) 
    '''
    def __init__(self):
        pass
    ''' 
    
    def abc(self): # 이름은 같지만 메소드임 (위의 함수랑 다름)
        print('메소드')
    def show(self):
        # kor = 80      # 지역변수
        print(self.kor) # MyClass의 kor 프린트 
        print(kor)      # show 메소드의 kor 프린트  # 만약 지역변수가 없다면 전역변수인 kor=100 을 참조
        self.abc()      # 메소드를 호출
        abc()           # 함수를 호출
        
my=MyClass()
my.show()