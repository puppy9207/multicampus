import sqlite3

# 파이썬 모듈 버전
print(sqlite3.version) #2.6.0
# SQLite3 설치 버전
print(sqlite3.sqlite_version)

conn = sqlite3.connect('book.db')
cursor = conn.cursor()

def dropTable(tableName):
    sql = 'drop table ?'
    cursor.execute(sql,tableName)
    conn.commit()

def createTable():
    sql = '''CREATE TABLE books(book_id integer primary key AUTOINCREMENT,
    title text unique not null, published_date date not null ,
    publisher text not null, pages integer not null, recommended integer);'''
    cursor.execute(sql)

def check_book(lists):
    print('리스트 여부 확인')
    if type(lists) != type([]):
        print('  리스트 아님')
        return False

    print('결측치 확인')
    if all(lists) == False:
        print('  결측치 발견')
        return False

    print('날짜 포맷 확인')
    date = lists[1]
    if len(date) != 8:
        print('  포맷에 맞지않음 8자리로 써주세요')
        return False

    if int(date[4:6]) >12 or int(date[4:6])<=0:
        print('  달을 확인해주세요')
        return False

    if int(date[6:8]) >31 or int(date[6:8])<=0:
        print('  일을 확인해주세요')
        return False

    recommend = float(lists[4])
    print('평점 확인')
    if recommend > 10 or recommend<0:
        print('  평점은 0이상 10이하의 숫자만 들어갈 수 있습니다')
        return False

    print(lists)
    return True




def insertTable():

    while True:
        print('-'*50)
        start = input('실행하시려면 아무키나 누르세요 끝내려면 q\n')
        print('-' * 50)
        if start == 'q' or start == 'Q':
            break
        checkList = []
        title = input('제목\n')
        checkList.append(title)
        date = input('날짜 ex)20180503\n')
        checkList.append(date)
        author = input('작가\n')
        checkList.append(author)
        page = input('페이지 수\n')
        checkList.append(page)
        recommend = input('평점\n')
        checkList.append(recommend)
        if check_book(checkList):
            commit = input('DB에 넣으시겠습니까? y를 누르면 들어갑니다\n')
            if commit == 'y' or commit == 'Y':
                sql = 'insert into books(title, published_date,publisher,pages,recommended) values(?,?,?,?,?)'
                cursor.execute(sql, checkList)
                conn.commit()
            else:
                print('넣지 않았습니다\n')
                continue


select = 'select * from books'
cursor.execute(select)
bookList = cursor.fetchall()
for i in bookList:
    print(i)

conn.close()

