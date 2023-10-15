# 웹문서 읽기 1
from urllib.request import urlopen  # 읽어올 때 쓰는 클래스 둘 중 하나만 쓰면됨
import requests
from bs4 import BeautifulSoup

#print('벅스 차트')
url = urlopen('https://music.bugs.co.kr/chart')
soup = BeautifulSoup(url.read(), 'html.parser')
#print(soup,type(soup)) # <class 'bs4.BeautifulSoup'>

musics = soup.findAll('td',class_='check')
print(musics)
for i,music in enumerate(musics):
    print("{}위:{}".format(i+1, music.input['title']))

print('--------------------------------------------------------------------------')

# 웹문서 읽기 2

import urllib.request as req

url = 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0'
wiki = req.urlopen(url)

soup2 = BeautifulSoup(wiki,'html.parser')
#mw-content-text > div.mw-parser-output > p:nth-child(6) 검사창에서 copy selector 해온 경로 (select 메소드에 줄 경로)
result = soup2.select('div.mw-parser-output > p > b') # 위 p요소에서 b만 선택해보자

for a in result:
    if(a.string != None):
        print(a.string)
        
print('-----------------------------------------------------------------------')
# 웹문서 읽기3 - daum의 뉴스 정보 읽기
url = 'https://news.daum.net/society#1'
daum = req.urlopen(url)

soup3 = BeautifulSoup(daum, 'lxml')
print(soup3.select_one('div > strong > a'))
data = soup3.select_one('div > strong > a')

for i in data:
    print(i)
    
datas = soup3.select('div > strong > a')

for i in datas[:5]:
    print(i)
    
print()
datas2 = soup3.findAll('a')
for i in datas2[:5]:
    h = i.attrs['href'],
    t = i.string
    print('href%s, text%s'%(h,t))