# 집합형 자료형 :  str, list, tuple, set, dict

# str - 순서 O : 인덱싱(한개의 값 참조), 슬라이싱(여러개의 값 참조)  수정 X

s='sequence'
print(s, type(s), len(s)) # sequence, s의 data type, s의 길이
print(s.count('e')) # e의 갯수
print(s.find('e'), ' ',s.find('e',3),s.rfind('e')) #e의 index 찾기 
#...

# 수정 불가
ss='mbc'
print(ss, id(ss))
ss='abc' # 수정이 아니라 참조값이 바뀐것 (id 값이 바뀌어있음)
print(ss, id(ss))

# 인덱싱 [index]
print(s[0], s[3]) # s[8] 같이 길이를 넘어가면 에러
print(s[-1], s[-3]) #뒤에서 1번째, 3번째 (-1부터 시작)

# 슬라이싱 [start:stop:step]
print(s[0:3]) # * 0'이상',  3'미만' = s[2]까지만 나옴
print(s[3:]) # 3번째 이상
print(s[:3]) # 3번째 미만
print(s[:]) # 전부다
print(s[1:5:2]) # [1] 부터 시작해서 [5] 미만까지 증가치가 2이다
print(s[-4:-1], s[-3:])
print('fre'+s[2:]) # 일부의 값만 참조해서 문자열과 연결 가능

print()
s2='kbs mbc'
s2=' '+ s2[:4]+'sbs '+s2[4:]+' '
print(s2, len(s2))
print(s2.strip()) # 좌우 공백 제거, lstrip()좌 공백 제거, rstrip()우 공백 제거
s3=s2.split(sep=' ') # 공백을 기준으로 자름 (흩뿌림)
print(s3)
print(' '.join(s3)) # ' ' 을 기준으로 합침

a='Life is too long'
b=a.replace('Life', 'Your leg') # replace('대상', '대체할str')
print(b)

