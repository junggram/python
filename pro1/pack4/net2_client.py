# 단순 클라이언트
from socket import *

clientsock=socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.7', 7878))     # 능동적으로 server에 접속, connect() 하면 server의 conn, addr = serversock.accept() 를 만남
clientsock.send('메루치보꾸메루치보꾸메루치보꾸메루치보꾸메루치보꾸메루치보꾸메루치보꾸메루치보꾸'.encode(encoding='utf-8'))       # encode() 로 요청을 보냄
re_msg=clientsock.recv(1024).decode()   # 수신
print('수신자료: ',re_msg)
clientsock.close()