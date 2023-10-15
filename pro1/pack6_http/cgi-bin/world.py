s1='나는'
s2='때려도 부서지지 않는 돌덩이'

print('Content-Type: text/html;charset=utf-8\n')
# html 형식을 한번에 넣을수도 있다
print('''
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
</head>
<body>
<h1>월드 페이지</h1>
자료 출력: {0}, {1}
<br>
<img src="../images/logo.png" width='30%',height='30%'/>
<br>
<a href="../index.html">홈으로</a>
</body>
</html>
'''.format(s1,s2))

