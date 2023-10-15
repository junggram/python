# file i/o with문

try:
    # 저장
    with open('file_test3.txt', mode='w',encoding='utf8') as f1:
        f1.write('파이썬으로 문서 가즈아\n')
        f1.write('with문을 쓰면\n')
        f1.write('명시적으로 close()를 하지 않는다')
        
    # 읽기
    with open('file_test3.txt', mode='r',encoding='utf8') as f2:
        print(f2.read()) # 한번에 읽어오기
        
        
except Exception as e:
    print('에러: '+e)
    
print('---'*5+'피클링(객체 저장)'+'---'*5)
import pickle
try:
    dictData={'소현':'111-1111','승경':'222-2222'}
    listData=['곡물 그대로의','새우깡']
    tupleData=(listData,dictData)
    # 개체를 저장
    with open('hello.data',mode='wb') as obj3: # mode='wb' 는 개체로 저장할때 (binary)
        pickle.dump(tupleData,obj3)
        pickle.dump(listData,obj3)
        
    # 개체를 읽기
    with open('hello.data',mode='rb') as obj4: # mode='rb' 는 개체를 읽어올때 
        a,b=pickle.load(obj4)
        print(a)
        print(b)
        c=pickle.load(obj4)
        print(c)
        
        
except Exception as e2:
    print('에러: '+e2)