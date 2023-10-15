#정규 표현식 : 다량의 데이터에서 원하는 데이터만 선택해서 처리할 때 효과적

import re
# from bokeh.models.glyphs import MultiLine

ss="12_1234 abc가나다abc_nbcABC_123555_6한국Python is fun."
print(ss)
print(re.findall('123', ss)) # list type으로 추출 (중복이 허용되기 때문)

print(re.findall(r'가나다', ss)) #정규표현식의 선행문자로 r을 써주는것을 권장
print(re.findall(r'[0-9]', ss)) #[ ]로 범위를 지정 (숫자만 = [0-9])
print(re.findall(r'[0-9]+', ss)) # + 는 반복되는 것을 포함 ( ['12', '1234', '123555', '6'] )
print(re.findall(r'[0-9]{2}', ss)) # *반복 횟수 ( ['12', '12', '34', '12', '35', '55'] )
print(re.findall(r'[0-9]{2,3}', ss))# *반복 2 또는 3 ( ['123', '123', '555'] )
print(re.findall(r'[a-z]+', ss)) # 영어 소문자만 반복 포함 ( ['abc', 'abc', 'ython', 'is', 'fun'] )
print(re.findall(r'[A-Za-z]+', ss)) # 영어 대소문자 반복 포함 ( ['abc', 'abcABC', 'Python', 'is', 'fun'] )
print(re.findall(r'[가-힣]+', ss)) # 한글만 반복 포함 ( ['가나다', '한국'] )
print(re.findall(r'[^가-힣]+', ss)) # 한글만 제외한 ( ['12_1234 abc', 'abcABC_123555_6', "'Python  is fun.'"] )
print(re.findall(r'12|34', ss)) # 12 or 34 ( ['12', '12', '34', '12'] )
print(re.findall(r'.bc', ss)) # .위치에는 아무거나 ( ['abc', 'abc', 'nbc'] )
print(re.findall(r'...', ss)) # ... 아무거나 세글자 ( ['12_', '123', '4 a', 'bc가', '나다a', 'bc_', 'nbc', 'ABC', '_12', '355', '5_6', "한국'", 'Pyt', 'hon', '  i', 's f', 'un.'] )
print(re.findall(r'[^1]+', ss)) # [^] 1을 제외하는 연속되는 ( ['2_', '234 abc가나다abc_nbcABC_', "23555_6한국'Python  is fun.'"] )
print(re.findall(r'^1+', ss)) # ^ 첫글자가 1인 ( ['1'] )
print(re.findall(r'fun.$', ss)) # $ fun.으로 끝나는

print(re.findall(r'\d', ss)) # 숫자만
print(re.findall(r'\d+', ss)) # 숫자만 반복 포함
print(re.findall(r'\d{1,3}', ss)) # 숫자만 1~3까지
print(re.findall(r'\s', ss)) # 공백만
print(re.findall(r'\S', ss)) # 모든 문자 (대문자 S)

print('---'*10) # flag 를 이용
p=re.compile('the', re.IGNORECASE) # the 를 대소문자를 구분하지 않기위한 객체생성 IGNORECASE
print(p)
print(p.findall('The dog the dog'))
print()
ss='''My name is tom.
I am happy'''
print(ss)
p=re.compile('^.+', re.MULTILINE) # ^.+ 처음에 어떤글자로 시작하던지, 두줄짜리를 한줄씩 찍어줌 MULTILINE
print(p.findall(ss))
