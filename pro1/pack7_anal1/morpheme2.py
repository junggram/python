# 웹문서를 읽어 형태소 분석(konlpy) 후 단어 빈도 수 등을 출력

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse # 한글 인코딩

okt = Okt()

# searchPara = input('검색단어: ')
searchPara = '이순신'
searchPara = parse.quote(searchPara) # 인코딩~
#print(searchPara)

url = 'https://ko.wikipedia.org/wiki/' + searchPara
page = urllib.request.urlopen(url).read().decode()
#print(page)

soup=BeautifulSoup(page,'lxml')

wordlist = []
#mw-content-text > div.mw-parser-output > p:nth-child(7)
for item in soup.select('#mw-content-text > div.mw-parser-output > p'):
    # print(item.string)
    if item.string !=None:
        wordlist+=okt.nouns(item.string)
        
print('wordlist :',wordlist,', 단어수 :',len(wordlist))

# {'당시':5, ....} 이렇게 출력 하려면
word_dict={} # 단어의 발생 횟수를 dict로 저장

for i in wordlist:
    if i in word_dict:
        word_dict[i]+=1
    else :
        word_dict[i]=1
    
print('발생 단어 수 : \n',word_dict)
print('발견된 단어 수 (중복 제거) :', str(len(set(wordlist))))
    
    
    