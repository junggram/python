# 예외처리 : 작업 중 발생하는 에러에 대처하기
# try ~ except

def divide(a,b):
    return a/b

print('이런저런 작업을 하다가...')

c=divide(5,2)
# c=divide(5,0) # ZeroDivisionError: division by zero
print(c)

print()
try:
    c=divide(5,2)
    #c=divide(5,0)
    print(c)
    
    aa= [1,2]
    print(aa[0])
    #print(aa[5])
    
    open('C:/abc.txt')
except ZeroDivisionError: # ZeroDivisionError일 때만 (안쓰면 모든 에러에 대해서) 
    print('에러 : 0으로 나눌 수 없습니다')
except IndexError as err: # IndexError일 때만
    print('에러 원인은', err)
except Exception as e: 
    print('기타 에러 : ',e)
finally:
    print('에러 유무에 상관없이 반드시 실행')
print('프로그램 종료')
