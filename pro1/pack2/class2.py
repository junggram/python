# 클래스

class Car: 
    handle=0 # Car type의 객체에서 참조 가능 멤버 필드
    speed=0
    
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed
        
    def showData(self): # Car type의 객체에서 참조 가능 멤버 메소드
        km='킬로미터'
        msg='속도:'+str(self.speed)+km,'핸들은: '+str(self.handle) # Car class의 필드를 부를 땐 self. 을 붙여야함
        return msg

print(id(Car))
print(Car.handle)
print(Car.speed)
print()
car1=Car('tom', 10) # 생성자 호출 후 self를 제외한 인자를 대입해서 객체 생성
print(car1.handle, car1.name, car1.speed)
car1.color='보라' # car1 고유의 멤버필드
print('car1 color: %s'%car1.color)
print('---')
car2=Car('james',20)
print(car2.handle, car2.name, car2.speed)
# print('car2 color: %s'%car2.color) #AttributeError: 'Car' object has no attribute 'color'
                        # car2에 color라는 고유멤버필드가 없다면 원형객체인 Car에 color가 있는지 확인하러 올라감
                        
print('주소: ',id(Car),id(car1),id(car2)) #서로 주소가 다름

print()
print(car1.showData())
print(car2.showData())
print(Car.showData(car2))
car2.speed=100   #고유멤버필드 수정
Car.handle=1   #원형클래스 멤버필드 수정
print(car1.showData())
print(car2.showData())
