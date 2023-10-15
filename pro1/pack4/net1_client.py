# 단순 클라이언트
from socket import *

clientsock=socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888))     # 능동적으로 server에 접속, connect() 하면 server의 conn, addr = serversock.accept() 를 만남
clientsock.send('ㅎㅇ반가워'.encode(encoding='utf-8',errors='strict'))       # encode() 로 요청을 보냄
clientsock.close()