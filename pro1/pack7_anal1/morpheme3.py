# 웹문서에서 검색된 자료 스크래핑 후 형태소 분석하고 난 다음 워드클라우드 작성
# donga.com에서 검색

# pip install pygame
# pip install simplejson
# pip install pytagcloud

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from konlpy.tag import Okt
from collections import Counter  # 카운팅 지원 모듈
import pytagcloud
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scrapy import item

# keyword = input('검색어 : ')
keyword = '낙옆' # 보수 좌파
targetUrl = "https://www.donga.com/news/search?query=" + quote(keyword)
print(targetUrl)  # https://www.donga.com/news/search?query=%EB%B6%81%ED%95%9C%EB%82%99%EC%98%86

source = urllib.request.urlopen(targetUrl)
soup = BeautifulSoup(source, 'lxml', from_encoding='utf-8')
# print(soup)

msg = ""

for title in soup.find_all('p', 'tit'):
    title_link = title.select('a')
    # print(title_link)
    articleUrl = title_link[0]['href']
    # print(articleUrl)
    try:
        source_article = urllib.request.urlopen(articleUrl)
        soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
        contents = soup.select('div.article_txt')
        # print(contents)
        for imsi in contents:
            item = str(imsi.find_all(text=True))
            # print(item)
            msg = msg + item
            
    except Exception as e:
        pass

print(msg)

okt = Okt()
nouns = okt.nouns(msg)
results=[]
for imsi in nouns: # 2글자 이상 명사만 작업에 참여
    if len(imsi)>1:
        results.append(imsi)
        
print(results)
count = Counter(results)
tag = count.most_common(50)  #빈도수가 높은 순으로 상위 50개만 작업
print(tag)

# 워드 클라우드
import pytagcloud
taglist = pytagcloud.make_tags(tag, maxsize = 100)
print(taglist[:10])

# tag_image 생성 후 저장
pytagcloud.create_tag_image(taglist,
                             output = '워드클라우드.png', #저장할 이름
                              size=(1000,600), # 저장할 크기 높이, 너비
                               background=(0,0,0),# 배경색
                                fontname='Korean', # 글꼴 
                                 rectangular=True) # 테두리 (border-radius 같은)

img = mpimg.imread('워드클라우드.png') # 확장자가 png이기 때문에 format 따로 안해도됨
plt.imshow(img)
plt.show()
