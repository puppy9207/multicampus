# class
# 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
# 장점
# 1. 코드의 재사용
# 2. 구조화
# 3.

# 함수 < 클래스 < 모듈 < 패키지
# 함수안에는 실행문 + 변수 + 리스트....
# 클래스 안에는 변수 개념을 속성(attribute)으로 지정
# 클래스에서 함수 개념을 메소드로 지정
# 클래스는 메소드의 집합
# 모듈은 파일간의 함수, 클래스 참조 가능
# 패키지는 모듈의 집합

# 클래스 생성
# 클래스 선언
class Square():
    # 생성자
    def __init__(self,width,height):
        self.width = width
        self.height = height



s1 = Square(50,100)
s2 = Square(20,50)
print(type(s1)) #인스턴스 <class '__main__.Square'>

# 인스턴스에서 속성값 부여
# 인스턴스이름.속성
print('s1의 가로',s1.width)
print('s1의 세로',s1.height)
print('s2의 가로',s2.width)
print('s2의 세로',s2.height)

# car 클래스 만들기
class car:
    def __init__(self,brand,name,color,price):
        self.brand = brand
        self.name = name
        self.color = color
        self.price = price

# 인스턴스 만들기
car1 = car('기아','스팅어','red',150000)
car2 = car('현대','스타렉스','Black', 520000)

# 퀴즈
# 주변에서 볼 수 있는 물체로 클래스를 선언하고
# 인스턴스화 시켜서 출력한다
class Book:
    def __init__(self,title,page,author,brand):
        self.title = str(title)
        self.page = int(page)
        self.author = str(author)
        self.brand = str(brand)

book1 = Book('점프 투 파이썬','3s36','박응용','이지스 퍼블리싱')
print(book1.page)