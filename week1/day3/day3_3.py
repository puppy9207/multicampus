# 비교 연산자
# 모든 리턴값이 True/False
a =1
b =1
print(a==b)
print(a!=b)

# 논리 연산자
# or 연산자
# T or T => T
# T or F => T
# F or T => T
# F or F => F
a=1
b=10
print((a==1) or (b==3)) #True
print((a==3) or (b==10)) #True
print((a==2) or (b==3)) #False


# and 연산자
# T and T => T
# T and F => F
# F and T => F
# F and F => F
a=1
b=10
print((a==1) and (b==10)) #True
print((a==1) and (b==8)) #False
print((a==3) and (b==10)) #False

# not 연산자
# not T -> F
a=1
print(not(a==1))
print(not(a<10))

print('*'*40)
# 조건제어문
# IF문
if True:
    print('조건제어문')

a=1
b=10
if a>b:
    print('a는 b보다 크다')

if a<b:
    print('a는 b보다 작다')

print('*'*40)
# 조건식에서 True가 되는 조건 = True , 1
# 조건식에서 False가 되는 조건 = False , 0

money = 0 # False
if money :
    print('택시를 타고')
print('가자')

money = 1000 # True
if money :
    print('버스를 타고')
print('가자')

money = None # False
if money :
    print('지하철을 타고')
print('가자')

print("-"*40)
# 퀴즈
data = int(input('정수를 입력해주세요\n'))

if data<0:
    print('음수')

if data>0:
    print('양수')

if data==0:
    print('0')


print("-"*40)
# 퀴즈2
age = int(input('나이를 입력해주세요 (숫자만) \n\n\n'))
if age>19:
    print('당신은 성인입니다')
else:
    print('당신은 성인이 아닙니다')