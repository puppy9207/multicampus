from flask import Flask

# app이라는 객체 생성
app = Flask(__name__)

# route 데코레이터 - URL 관리
@app.route("/")
# 뷰 함수 -> 화면 표시 함수
def hello():
    return "<h1 style='text-align:center'>Hello World!</h1>" \
           "<p><a href='/users/pap'>test</a></p>" #텍스트, html 태그 가능

@app.route("/users/<userid>/<username>")
def users(userid,username):
    return 'users is %s, username is %s' % (userid,username)

# 값 제한
@app.route('/news/<int:newsid>/<int:start>')
def news(newsid,start):
    return '뉴스 %s %s' % (newsid,start)

@app.route('/bbs/<int:bbsnum>/<content>')
def bbs(bbsnum,content):
    return '글번호 : %s <br> 내용 : %s' % (bbsnum,content)
if __name__ == "__main__":
    app.run()