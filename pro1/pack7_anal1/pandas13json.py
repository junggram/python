# web에서 JSON 문서 읽기
# JSON 은 Beautiful Soup이 필요가 없다
import json
import urllib.request as req

url = 'https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.json'
plainText = req.urlopen(url).read().decode() # json 문서 웹에서 가져오기
#print(type(plainText))           # <class 'str'>

jsonData = json.loads(plainText)    # str --> dict : json 디코딩
#print(type(jsonData))            # <class 'dict'>

print()
# print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME']) # B.S가 필요없다

libDatas = jsonData.get('SeoulLibraryTime').get('row')
# print(libDatas)

datas = []

for ele in libDatas:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name + '\t' + tel + '\t' + addr)
    imsi = [name,tel,addr]
    datas.append(imsi)

import pandas as pd
df = pd.DataFrame(datas, columns=['도서관 이름', '전화번호', '주소'])
print(df)
df.to_html('도서관정보.html')