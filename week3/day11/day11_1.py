import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='shop')
cursor = conn.cursor()

def select_order():
    sql = 'select * from orders'
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(*i)

insertSQL = 'insert into orders values(%s,%s,%s,%s)'
data = [('123','우유','20180813','서울시 중랑구'),
        ('152','커피','20180615','서울시 동대문구'),
        ('167','커피','20180408','경기도 부천시'),
        ('158','천일염','20180608','서울시 중랑구'),
        ('913','쌀','20171231','강원도 원주시')
        ]

cursor.executemany(insertSQL,data)
conn.commit()


select_order()
conn.close()