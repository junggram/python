import numpy as np
import pandas as pd

data = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print(data[::-1,::-1])

x = [1,2,3,4,5]
x = np.array([1,2,3,4,5])
y = np.arange(1,4).reshape(3,1)
print(x+y)


df = pd.read_csv('ex.csv', names=['a','b'])

print(df)

df=pd.DataFrame(np.arange(12).reshape((4,3)), index=['1월','2월','3월','4월'], columns=['강남','강북','서초'])

print(df)

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"

res = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(res, 'lxml')

items = soup.select('#tabCont01 > ul > li > a > dl > dt')
chi=[]
for item in items:
    chi.append(item.string)
    
prices = soup.select('#tabCont01 > ul > li > a > p.money > strong')
chip=[]
for price in prices:
    chip.append(int(price.string.replace(',','')))
    
data = {
        '상품명':chi,
        '가격':chip
    }
df = pd.DataFrame(data)
print(df)
print('가격평균 :',df['가격'].mean())
print('가격표준편차 :',df['가격'].std())

