# class의 상속 : 다형성을 구사할 수 있다 (메소드 override 가능)
# 보통 상속은 다른 파일로 만들어두고 import 해야하지만 여기선 그냥 같은 클래스 내에서 사용함
class Animal:
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal): # ( )를 열고 부모클래스를 인자로 넣어주면 "상속" 
    def __init__(self):
        print('Dog 생성자') # Dog의 생성자가 있으면 Animal 생성자는 자동으로 호출되지 않는다 (강제로 호출하지 않는 이상)
                          # Dog의 생성자가 없으면 콘솔창에는 Animal(부모) 생성자가 호출됨
    def my(self):
        print('난 댕댕이')

dog1=Dog() # Animal을 넣지 않아도 상속이 되어있음
dog1.move()
dog1.my()

print()
class Horse(Animal):
    pass

horse1=Horse() # Horse의 생성자를 안썼으므로 Animal 생성자가 호출됨
horse1.move()


