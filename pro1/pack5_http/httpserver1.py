# 웹 서버 구축

from http.server import SimpleHTTPRequestHandler,HTTPServer # 정적인 표현밖에 못함 (cgi가 없기 때문에)
# HTTPServer : 기본적인 socket 연결을 관리
# SimpleHTTPRequestHandler : 요청을 처리 (대표적으로 get,post)

port=7777
handler=SimpleHTTPRequestHandler
serv=HTTPServer(('127.0.0.1',port),handler)     # 서버 바인딩 (주소를 줘야함)
print('웹 서비스 자 드가자')
serv.serve_forever()

