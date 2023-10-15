# 서버 무한 루핑
import socket
import sys

#HOST='127.0.0.1'
HOST='192.168.0.19'
PORT= 7979

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    serversock.bind((HOST, PORT))
    serversock.listen(5)    # 동시 접속 최대 수 설정(1~5)
    print('server start...')
    
    while True:
        
        conn, addr = serversock.accept()   # 연결 대기
        print('client info: ', addr[0], addr[1])   #ip addres, port number 확인
        print('from client message :', conn.recv(1024).decode())  # 메세지 수신
        
        
        # 메세지 송신 
        conn.send(('from server: '+str(addr[0])+'야!!!!최자드!!!!!야!!!!최자드!!!!!야!!!!최자드!!!!!야!!!!최자드!!!!!야!!!!최자드!!!!!').encode('utf_8'))
        
except socket.error as err:
    print('err : ', err)
    sys.exit()
finally:
    serversock.close()
