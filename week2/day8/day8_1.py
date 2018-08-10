# 웹스크래핑
# html페이지에서 필요한 정보만 추출하는 기능
from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
html = urlopen('http://www.naver.com')
bs = BeautifulSoup(html.read(),'html.parser')
print(bs)
print('-'*50)
# 특정태그만 추출하기
# bs.태그이름
print(bs.div)
# bs.태그.태그 이런식도 가능하다
print(bs.div.a)
# String 만 추출하는것도 가능
print('-'*50)
print(bs.h1.span)
print(bs.h1.span.string)
print('-'*50)
# 아이디를 찾아서
print(bs.find(id='veta_time2'))
'''
#html 태그를 변수로 지정해서 연습하기
html = """
<html>
    <body>
     <ul>
        <li class="fruit">사과</li>
        <li>양파</li>
        <li>고구마</li>
        <li class="fruit">바나나</li>
     </ul>
    </body>
</html>
"""
bs = BeautifulSoup(html,'html.parser')
fruitList = bs.find_all(class_="fruit")
for i in fruitList:
    print(i)

for i in fruitList:
    print(i.string)