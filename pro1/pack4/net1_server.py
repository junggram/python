# client / server (echo server) 프로그래밍
# server 

from socket import *

# socket으로 서버 구성
serversock=socket(AF_INET,SOCK_STREAM)      # socket(소켓종류, 소켓유형)
serversock.bind(('127.0.0.1', 8888))    # ip주소와, port번호
serversock.listen(1)    # 동시접속 최대 수 설정(1 ~ 5)
print('server 시작')

conn, addr = serversock.accept()    # 연결 대기
print('addr:', addr)
print('conn:', conn)
print('from client message:',conn.recv(1024).decode())      # 받아온 클라이언트의 요청(인코딩되어서 패킷형식으로 전송)을 다시 디코딩
conn.close()
serversock.close()