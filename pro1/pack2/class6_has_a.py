# 냉장고에 음식 담기 - 클래스의 포함관계 구현

class Fridge:
    isOpened=False
    foods=[]
    
    def open(self):
        self.isOpened=True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened==True:
            self.foods.append(thing) #포함
            print('냉장고 안에 음식을 저장함')
            self.food_list()
        else:    
            print('문열어 쾅쾅쿠아콰아쾅')
            
    def close(self):        
        self.isOpened=False
        print('냉장고 문 닫기')
        
    def food_list(self):
        for f in self.foods:
            print(f.irum,f.exp)
        print()
        
        
class FoodData:
    def __init__(self,irum,exp):
        self.irum=irum
        self.exp=exp
        
if __name__=='__main__':
    
    f=Fridge()
    apple=FoodData('사과','2022-10-15')
    f.open()
    f.put(apple)
    f.close()
    print()
    minfe=FoodData('민철','2088-11-11')
    f.open()
    f.put(minfe)
    f.close()
    

    