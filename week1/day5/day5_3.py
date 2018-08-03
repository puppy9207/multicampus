# 클래스 생성
# def __init__(self,인자) -> 생성자 함수(속성)
# def 메소드이름(self,인자):

class Person:
    def __init__(self,name,age,height,gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    def get_gender(self):
        return self.gender

    def set_name(self,name):
        self.name = name

    def walk(self):
        print('걷는다')

    def info(self):
        print('이 사람의 이름은 %s입니다.' % self.name)
        print('나이는 %d이고, 키는 %d이고 %s입니다.'%(self.age,self.height,self.gender))


p1 = Person('고주원',24,173,'남자')
p1.info()
print(p1.get_age())

# 사각형 클래스 생성 후 사각형의 속성을 출력하는 메소드 정의
class Square():
    def __init__(self,weight,height):
        self.weight = int(weight)
        self.height = int(height)

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def area(self):
        return self.weight*self.height

s1 = Square(50,100)
print(s1.area())

class Circle:

    def __init__(self,rad):
        self.rad = rad

    def get_rad(self):
        return self.rad

    def get_dia(self):
        return self.rad*2

    def get_area(self):
        import math
        result = (self.rad**2)*math.pi
        result = "%.3f" % result
        result = float(result)
        return result

c1 = Circle(6)
print(c1.get_area())

class Calcul:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2


    def getSum(self):
        return self.n1+self.n2

    def getMin(self):
        return self.n1-self.n2

    def getMul(self):
        return self.n1*self.n2

    def getDiv(self):
        return self.n1/self.n2
