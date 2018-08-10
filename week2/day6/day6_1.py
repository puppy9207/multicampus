# 모듈
# 별도의 파일(.py)로 제작
# 내부모듈 - 기본적으로 제공
# 외부모듈 - 설치후 사용 가능
# 사용자 정의 모듈 - 직접 제작해서 사용
# 모듈은 import로 불러온다
import math as m # 모듈 전체를 불러옴

print(m.pi)
print(m.sin(5))

from math import pi,sin # 이렇게 특정 함수만 불러와도 된다.

import random as rd
print(rd.randrange(100))
print(rd.randrange(1,50))

choice = ['a','av','ae','aaw','rar']
print(rd.choice(choice))

import sys
print(sys.argv) # 현재 문서의 경로
print(sys.version) #

import os
print('-'*15)
print(os.name)
print(os.getcwd())
print(os.listdir)
