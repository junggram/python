# Beautiful soup 클래스가 제공하는 searching 관련 method

from bs4 import BeautifulSoup

html_page = '''
<html><body>
<h1>제목 태그</h1>
<p>웹 문서 스크래핑</p>
<p>특정 페이지 문서</p>
</body></html>
'''
print(type(html_page)) # <class 'str'>

soup = BeautifulSoup(html_page,'html.parser')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
print(soup)

 
print()
h1 = soup.html.body.h1 
print('h1:',h1, type(h1)) # <class 'bs4.element.Tag'>
print('h1:',h1.string, type(h1.string)) # <class 'bs4.element.NavigableString'>
print('h1:',h1.text, type(h1.text)) # <class 'str'>

print()
p1 = soup.html.body.p # 첫번째 p요소
print('p1:',p1.string)

p2 = p1.next_sibling.next_sibling # 두번째 p요소 # 이런식으로 요소를 하나하나 찾기엔 너무 힘들다
print('p2:',p2.string)

print('\n검색용 메소드 : find()')
html_page2 = '''
<html><body>
<h1 id='title'>제목 태그</h1>
<p>웹 문서 스크래핑</p>
<p id='my' class='our'>특정 페이지 문서</p>
</body></html>
'''
soup2 = BeautifulSoup(html_page2, 'html.parser')
print(soup2.p,' ', soup2.p.string) # 첫번째 p요소
print(soup2.find('p').string) # 위와 같음 # find()는 먼저 선택된 element만 선택됨
print(soup2.find(['p','h1']).string) # 변수를 복수로 써줄 수 있지만 # find()는 한개만 넘어옴
print(soup2.find(id='title').string)
print(soup2.find(id='my').string)
print(soup2.find(class_='our').string) # class는 _를 붙여줘야함

print(soup2.find(attrs={'class':'our'}).string) # attrs 에 dict 형식으로 넣어줘도 됨
print(soup2.find(attrs={'id':'my'}).string)

print('\n검색용 메소드 : findAll(), find_all()')
html_page3 = '''
<html><body>
<h1 id='title'>제목 태그</h1>
<p>웹 문서 스크래핑</p>
<p id='my' class='our'>특정 페이지 문서</p>
<div>
    <a href="https://www.naver.com" class='aa'>naver</a><br/>
    <a href="https://www.daum.net" class='aa'>daum</a>
</div>
</body></html>
'''
soup3 = BeautifulSoup(html_page3, 'html.parser')
print(soup3.find_all('p')) # p요소를 모두 찾아줌
print(soup3.find_all('a'))
print(soup3.find_all(['a','p'])) # 변수를 복수로 사용할 수 있다
print(soup3.find_all(class_='aa'), '클래스') # 속성명으로 선택해서 찾을 수 있다
print(soup3.findAll('p'), '대문자 All') # 이름만 다를뿐 위와 같은 메소드이다 

print()
links = soup3.findAll('a')
for i in links:
    print(i.attrs['href'],' - ',i.string) # 응용
    
print('정규 표현식')

import re # regular expression

links2 = links = soup3.findAll(href=re.compile(r'^https'))
for i in links2:
    print(i.attrs['href'],' - ',i.string)

print('\nCSS의 selector 사용')
html_page4 = '''
<html><body>
<div id='hello'>
    <a href="https://www.naver.com" class='aa'>naver</a><br/>
    <span>
        <a href="https://www.daum.net" class='aa'>daum</a>
    </span>
    <ul class='world'>
        <li>안녕</li>
        <li>반갑</li>
    </ul>
</div>
<div id='hi' class='good'>
    second div
</div>
</body></html>
'''
soup4 = BeautifulSoup(html_page4, 'html.parser')
print(soup4.select_one('div'))              # 첫번째 div 태그만 선택됨    # select_one()은 단수를 반환
print()
print(soup4.select_one('div#hi'))           # id가 hi인 div가 선택됨
print(soup4.select_one('div.good'))         # class가 good인 div가 선택됨
print()
print(soup4.select('div'))                  # select()은 복수를 반환
print(soup4.select('div#hello > a'))        # 자식 (직계)
print(soup4.select('div#hello a'))          # 자손
print(soup4.select('div#hello > span > a')) # span 안의 <a>태그만 선택

lis = soup4.select('div#hello ul.world > li') # li 요소 선택

print(lis)
msg = list() # []
for i in lis:
    msg.append(i.string)
    
import pandas as pd
df = pd.DataFrame(msg, columns = ['자료'])    # 받은 자료를 pandas의 DataFrame으로 만들어보기
print(df)