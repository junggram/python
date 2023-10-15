# 기상청 제공 날씨 정보 XML 자료 읽기
# https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from pandas.tests.frame.methods.test_sort_values import ascending

url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(data,'html.parser')
# print(soup)

# find method
title = soup.find('title').string
print(title)
wf = soup.find('wf').string
print(wf)

city = soup.find_all('city')
print(city)
cityData = []
for c in city:
    cityData.append(c.string)
    
df = pd.DataFrame()
df['city'] = cityData
print(df.head(3))

print()
# select method
tempMins = soup.select('location > province + city + data > tmn') # +로 next_sibling을 대신함  #  +는 아래로 -는 위로

tempData = []

for t in tempMins:
    tempData.append(t.string)
    
df['temp_min'] = tempData
df.columns = ['지역','최저기온']
print(df.head(3))

df.to_csv('날씨.csv',index=False)
print()
df2 = pd.read_csv('날씨.csv')
print(df2.head(3))

print('----------df 자료로 슬라이싱----------')
# iloc (숫자 기반)
print(df.iloc[0])

print(df.iloc[0:2,:])
print(df.iloc[0:2,0:1])
print(df.iloc[0:2,0:2])
print()
print(df['지역'][0:2]) # Series
print()
print(df['지역'][:2]) # Series

# loc (라벨 값 기반)
print(df.loc[1:3]) # index를 참조하여 
print(df[1:4])
print(df.loc[[1,3]])
print(df.loc[:,'지역'].head(2)) # Series
print(df.loc[1:3,['최저기온','지역']]) #loc
print(df.loc[:,'지역'][1:4])

print('------')
df = df.astype({'최저기온':int}) # 형변환 
print(df.info())
print(df['최저기온'].mean(),' ',df['최저기온'].std()) # 숫자로 바뀌었기 때문에 함수로 연산이 가능 (평균, 표준편차 등등)

print(df['최저기온'] >= 6) # True False

print(df.loc[df['최저기온'] >= 7]) # 위의 True False로 결과를 추출

print(df.sort_values(['최저기온'], ascending=True)) # 정렬 기능


