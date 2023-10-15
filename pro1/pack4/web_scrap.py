# 멀티 프로세싱으로 웹 스크래핑
# https://beomi.github.io/beomi.github.io_old/        # 연습용 사이트

import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_links():    # a tag의 주소를 읽기
    data=requests.get('https://beomi.github.io/beomi.github.io_old/').text
    soup=bs(data,'html.parser')     # html.parser로 구조파악
    # print(soup)
    my_titles=soup.select(          # select로 빼냄(선택)
        'h3 > a'  # h3의 자식요소인 a를 뜻함
    )
    data=[]
    
    for title in my_titles:
        data.append(title.get('href'))
        
    return data

def get_content(link):  # a tag에 의한 해당 사이트 문서 내용 중 일부 문자값 읽기
    abs_link='https://beomi.github.io'+link     # 완성된 형태의 링크
    #print(abs_link)
    req=requests.get(abs_link)                  # requests.get으로 링크로 이동해서 있는 정보를 불러옴
    html=req.text                               # 불러온 정보를 text형식으로 
    soup=bs(html,'html.parser')                 # html.parser로 구조를 파악해서
    # 가져온 자료로 뭔가를 실행한다
    print(soup.select('h1')[0].text)            # 읽어올 자료를 선택해서 콘솔창에 출력
    
if __name__=='__main__':
    start_time=time.time()
    print(get_links())
    print(len(get_links()))
    
    ''' 직렬연결 : 2.1초
    for link in get_links():
        get_content(link)
    print('처리 시간: {}'.format(time.time() - start_time))
    '''
    
    ''' 병렬연결 :0.9초
    pool= Pool(processes=4) 
    pool.map(get_content, get_links())  # map(실행할 함수, 데이터를 불러올 함수)
    print('처리 시간: {}'.format(time.time() - start_time))
    '''