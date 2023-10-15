# 일정 시간 마다 웹 문서 읽기 (scheduler) 
# 동적인 data를 읽을 때 사용 (ex = 주식, 현재인원 등등)

# import schedule # pip install schedule    스케쥴러 모듈 지원

import time
import datetime
import urllib.request as req
from bs4 import BeautifulSoup
import requests

def work():
    url = 'https://finance.naver.com/marketindex/'
    # data = req.urlopen(url)        # 방법 1 데이터를 보낼 때 인코딩하여 바이너리 형태로 보낸다
    data = requests.get(url).text    # 방법 2 데이터를 보낼 때 딕셔너리 형태로 보낸다
    
    soup = BeautifulSoup(data, 'html.parser')
    price = soup.select_one("div.head_info > span.value").string
    print('미국USD :',price)
    
    t = datetime.datetime.now() # 현재 시간
    fname = './USD/' + t.strftime('%Y-%m-%d-%H-%M-%S') + '.txt' # 경로와 파일명을 지정 - 현재 날짜 및 시간
    
    with open(fname, 'w') as f: # 파일 저장
        f.write(price)
        
while True:
    print('recall')
    work()
    time.sleep(5) # 5초 마다 work() 함수 호출
    
    # if 문을 이용해서 마감시간을 정할수도 있다