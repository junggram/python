# 다중 상속 : 순서가 중요

class Tiger:
    data='호랑이세상'
    
    def cry(self):
        print('에힝')
        
    def eat(self):
        print('맹수는 고기를 좋아해')
        
class Lion:
    
    def cry(self):
        print('으르렁 으르렁 대')
        
    def hobby(self):
        print('갓수의 왕은 나야나')
        
class Liger1(Tiger, Lion):  # 다중 상속
    pass

a1=Liger1()
a1.cry() # 호랑이의 cry()를 호출 , 다중 상속에선 순서가 중요, 인자로 넣는 순서대로 우선권이 부여됨
a1.eat()
a1.hobby()
print(a1.data)

print('---')
class Liger2(Lion, Tiger):
    data='라이거 만세'
    
    def hobby(self):
        print('라이거는 자바가 마렵다')
        
    def showData(self):
        print(self.data,' ', super().data)
        self.hobby() # 자식의 메소드 호출
        super().hobby() # 부모의 메소드 호출
a2=Liger2()
a2.cry()
a2.hobby() # override한 메소드를 호출
a2.showData() # Liger2의 고유 메소드를 호출함