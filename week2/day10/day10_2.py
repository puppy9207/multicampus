import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
def create_table():
    sql = '''
    create table subject (sub_num varchar(20) not null, sub_name text not null, prof_name text not null,
    prof_code integer not null, class_code varchar(20) not null, class_descript text)
    '''
    conn.execute(sql)

def insert_table():
    sql = 'insert into subject values(?,?,?,?,?,?)'
    data = [('DBO101','오라클기초','서영학',21,'A301','공대301호'),
            ('DBO101', '오라클기초', '서영학', 21, 'A301', '공대301호'),
            ('DBO101', '오라클기초', '서영학', 21, 'A301', '공대301호'),
            ('DBO101', '오라클기초', '서영학', 21, 'A301', '공대301호'),
            ('DBO101', '오라클기초', '김이교', 22, 'A302', '공대302호'),
            ('DBM101', 'vlsSQL기초', '서영학', 21, 'B301', '인문대301호'),
            ('DBM101', 'vlsSQL기초', '서영학', 21, 'B301', '인문대301호'),
            ('JAVA102','자바중급','이민우',23,'A301','공대301호')
            ]
    cursor.executemany(sql,data)
    conn.commit()

def select_table():
    sql = 'select * from subject'
    cursor.execute(sql)
    sub_list = cursor.fetchall()
    for i in sub_list:
        print(i)

def delete_table():
    sql = 'delete from subject where sub_name="자바중급"'
    cursor.execute(sql)

def update_table():
    sql = 'update subject set class_descript="공대505호" where class_descript="공대301호"'
    cursor.execute(sql)

def select_detail():
    sql = 'select * from subject where prof_code=21'
    cursor.execute(sql)
    sub_list = cursor.fetchall()
    for i in sub_list:
        print(i)

select_detail()