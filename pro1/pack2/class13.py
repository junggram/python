# 상속

class ElecProduct:
    volume=0
    
    def volumeControl(self,volume):
        pass
    
class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume+=volume
        print('ㅆㅍ 소리 크기 : ', self.volume)
        
class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        imsi=self.volume+volume
        self.volume = imsi
        print('ElecRadio 볼륨 크기는', self.volume)
        
tv=ElecTv()
radio=ElecRadio()

abc=tv.volumeControl(3)

radio.volumeControl(10)