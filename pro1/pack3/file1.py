# file i/o (input, output)

import os
print(os.getcwd()) # 현재 절대 경로 알아내기

try:
    print('읽기------')
    # f1=open(r'C:\work\pro1\pack3\file_test.txt', mode='r', encoding='utf8') # 모드와 인코딩
    # f1=open(os.getcwd()+'\\file_test.txt', mode='r', encoding='utf8') # 같은 코드
    f1=open('file_test.txt',mode='r',encoding='utf8') # mode='r' 은 읽기   mode='r','w','a','b'...
    print(f1)
    print(f1.read()) # 읽기
    f1.close() # 파일을 열었으면 닫아줘야함
    
    print('저장------')
    f2=open('file_test2.txt',mode='w',encoding='utf8') # mode='w' 는 (저장)덮어쓰기
    f2.write('My Friends\n')
    f2.write('홍길동, 나길동')
    f2.close()
    
    print('추가------')
    f3=open('file_test2.txt',mode='a',encoding='utf8') # mode='a' 는 추가
    f3.write('\n손오공')
    f3.write('\n팔계')
    f3.write('\n오정')
    f3.close()
    
    print('읽기------')
    f4=open('file_test2.txt',mode='r',encoding='utf8')
    print(f4.readline()) # 한줄씩 읽기
    print(f4.readline())
    f4.close()
except Exception as e:
    print('에러: ',e)