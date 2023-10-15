# 동 이름을 입력해 해당 동의 우편번호 및 주소 출력

try:
    dong=input('동 이름 입력:')
    
    with open('zipcode.txt',mode='r',encoding='euc-kr') as f:
        line=f.readline() 
        # print(line)
        while line: # 읽을 문자열이 있다면
            # lines=line.split('\t') # \t(탭)을 기준으로 자르고 list로 반환
            lines=line.split(chr(9)) # 위 코드와 같은 말 ascii(아스키)코드 표의 값을 넣은것
            # print(lines)
            if lines[3].startswith(dong):
                # print(lines)
                print('['+lines[0]+']'+lines[1]+' '+lines[2]+' '+lines[3]+' '+lines[4])
                
            line=f.readline()
            
except Exception as e:
    print('에러: '+e)