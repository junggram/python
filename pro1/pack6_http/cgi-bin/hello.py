# 웹 서비스 대상 파일
kor=50
eng=60
tot=kor+eng
print('Content-Type: text/html;charset=utf-8\n') # 콘솔 x 웹브라우저로 전송하는 print(),  text/html = mime 타입
print('<html><body>')
print('<b>안녕하세요 케케케</b> 파이썬 모듈로 작성했어요<br>')
print('총점은 %s'%(tot)) # 파이썬의 기능을 사용해서 데이터 출력도 가능 (마치 jsp파일 같음)
print('<a href="../index.html">홈으로</a>')
print('</body></html>')
