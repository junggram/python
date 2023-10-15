# 웹 서버 구축

from http.server import CGIHTTPRequestHandler,HTTPServer # cgi 덕분에 동적인 표현이 가능함
# CGIHTTPRequestHandler : 동적으로 웹서버를 운영이 가능하게 하는 객체
# CGI : 웹서버와 웹프로그램 사이에서 정보를 주고받는 방법 또는 규약

port=8888

class Handler(CGIHTTPRequestHandler):
    
    cg_directories = ['/cgi-bin'] # cgi효과를 넣어줄 파이썬파일의 경로를 알려줌

serv=HTTPServer(('127.0.0.1',port),Handler)     # 서버 바인딩 (주소를 줘야함)
print('웹 서비스 자 드가자')
serv.serve_forever()