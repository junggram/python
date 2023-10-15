# 사용자가 전송한 정보를 수신 후 ... 

import cgi # 정보를 받기위해 common gate interface 를 사용

form=cgi.FieldStorage() # 전송받은 정보를 저장

irum=form["name"].value 
phone=form["phone"].value
gen=form["gen"].value

print('Content-Type: text/html;charset=utf-8\n')
print('''
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
</head>
<body>
이름은 {0}
<br>
핸드폰 {1}
<br>
성별은 {2}
</body>
</html>
'''.format(irum,phone,gen))