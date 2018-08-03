# 상속
# 상속이란 다른 클래스의 기능을
# 물려받을 수 있게 정의

# 부모 클래스 정의
class Phone:

    #속성 정의
    def __init__(self,kind):
        self.kind = kind


    def info(self,kind):
        print(' 종류 %s' %self.kind)

class Internet:
    def __init__(self,wifi):
        self.wifi = wifi

    def info(self,wifi):
        print('aaa',wifi)
# phone을 상속받음
# 다중상속이 가능하네
class Mobile(Phone,Internet):
    pass

m = Mobile('갤럭시')
m.info('a')