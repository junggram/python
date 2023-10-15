# 웹 문서 읽기 (scraping)
# crawling : scrap, selenium ...
# Beautiful soup을 이용 : XML, HTML 문서 처리

import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.naver.com/index.html"
sourceData = requests.get(baseUrl)
print(sourceData)

plainText = sourceData.text # 웹에서 소스 불러오기까지 완료
#print(plainText)
print(type(plainText)) # <class 'str'> 하지만 스트링타입임

convertData = BeautifulSoup(plainText, 'lxml') # Beautiful soup 객체 생성과 Parser를 사용
#print(convertData)
print(type(convertData)) # <class 'bs4.BeautifulSoup'> 뷰티풀숲 객체가 되었음

for atag in convertData.find_all('a'): # 웹브라우저 소스에있는 <a> 만 찾아와보기
    href = atag.get('href') # <a>의 href속성과
    title = atag.string # <a>의 String
    print(href,' ',title) # 출력
    
