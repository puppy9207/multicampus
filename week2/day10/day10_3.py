import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='myko')
cursor = conn.cursor()
cursor.execute('select * from student')
ls = cursor.fetchall()
for i in ls:
    print(i)