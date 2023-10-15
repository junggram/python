# 가수 한명을 탄생

# import pack2.class4
from pack2.class4 import SingerType

def process():
    # young=pack2.class4.SingerType()
    young=SingerType()
    print('영웅의 타이틀 곡: ', young.title_song)
    young.sing()

def process2():
    bts=SingerType()
    bts.sing()
    bts.title_song='민철이와 민 오브리'
    print('bts의 타이틀 곡: ', bts.title_song)
    bts.sing()
    bts.co='하이브'
    print('소속사: '+bts.co)
    print()
    blackpink=SingerType()
    blackpink.sing()
    blackpink.title_song='shoot down'
    print('blackpink의 타이틀 곡: ', blackpink.title_song)
    blackpink.sing()
    blackpink.co='YG'
    print('소속사: '+blackpink.co)
# process() 이렇게 써도 되지만

if __name__=='__main__': # 가독성을 위해 main 모듈을 알리는 코드를 입력하는 것을 권장
    process()
    process2()