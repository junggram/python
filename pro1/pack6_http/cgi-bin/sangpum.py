# MariaDB 자료 웹으로 출력

import MySQLdb
import pickle

with open('mydb.dat',mode='rb') as obj: # 위 대신 mydb.dat로 내 db정보를 불러오는 것으로 (암호화 + 간편함)을 확보
    config =pickle.load(obj)
    
print('Content-Type: text/html;charset=utf-8\n')
print('<html>')
print('<body>')
print('<h2>상품 정보</h2>')
print('<table border="1px">')
print('''<tr>
        <th>코드</th>
        <th>품명</th>
        <th>수량</th>
        <th>단가</th>
    </tr>''')
try:
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    
    cursor.execute("select*from sangdata")
    datas=cursor.fetchall()
    for code,sang,su,dan in datas:
        print('''
            <tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
            </tr>
        '''.format(code,sang,su,dan))
except Exception as e:
    print('처리오류:',e)
finally:
    cursor.close()
    conn.close()
print('</table>')
print('</body>')
print('</html>')