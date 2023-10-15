'''
class coffeeMachine:
    def showData(self, cupCount, change):
        print('커피 %d잔과'%cupCount, '잔돈 %d원'%change)

class coinIn:
    coffeePrice=200
    
    def __init__(self):
        self.data = coffeeMachine() # 클래스의 포함
    def culc(self):
        
        coin=int(input('동전을 넣으세요 : '))
        if coin == 200:
            self.data().showData(1, 0)
        elif coin == 400:
            self.data().showData(2, 0)
        else:
            print('요금이 부족합니다.')  

if __name__ == '__main__':
    coinIn().culc() 
'''

class CoinIn:
    
    def insert(self):
        self.coin=int(input('동전을 넣어주세요'))
        return self.coin
class Machine:
    
    def showData(self):
        
        print('커피는 한잔에 200원 입니다')
        coin=CoinIn().insert()
        count=int(input('몇잔을 원하세요?'))
        
        if 200*count > coin:
            print('요금이 부족합니다')
        elif 200*count <= coin:
            refund=coin-(200*count)
            print('커피 %d잔과'%count,'잔돈 %d원'%refund)
        
if __name__=='__main__':
    Machine().showData()