# 함수(function)
# 함수는 명령문의 조합
# 함수 < 클래스 < 모듈 < 패키지

# 함수정의 문법
# def 함수명(입력인수):
#   <수행할 문장>
'''
    def fun():
        print('하하하')
        return '재밌다'
'''

# 받은 글자를 3번 출력하는 함수 정의
def threePrint(a):
    print(a*3)

# 함수 호출
threePrint('aaa')

# 함수의 종류
# 인자 x, 결과값(return) x
def maybe():
    print('아마도 뭔가...')
# 인자 o, 결과값(return) x
def inMaybe(a):
    print('아마도 %d가..'% a)
# 인자 x, 결과값(return) o
def outMaybe():
    return '아마도 배출되는 무언가..'
# 인자 o, 결과값(return) o
def inOutMaybe(a):
    print('아마도 a가 들어오고 뭔가 나가겠지?')
    b = a+2
    return b

print(inOutMaybe(3))

# 퀴즈 인자값을 받아서 구구단 출력
def gugudan(n):
    for i in range(1,10):
        print('%d * %d = %d' % (n,i,(n*i)))

gugudan(4)

# 리턴값이 여러개도 가능하다!!
def sum_and_mul(a,b):
    return a+b, a*b

print(sum_and_mul(4,5)) #튜플 형태로 배출
aSum = sum_and_mul(4,5)[0]
aMul = sum_and_mul(4,5)[1]
print('두 개의 합은 %d , 두 개의 곱은 %d' % (aSum,aMul))

# BMI 함수로
def bmi(height,weight):
    calBmi = float(weight/((height/100)**2))
    if calBmi>35:
        return '고도 비만'
    elif calBmi>=30 and calBmi<35:
        return '중증도 비만'
    elif calBmi>=25 and calBmi<30:
        return '경도 비만'
    elif calBmi>=23 and calBmi<25:
        return '과체중'
    elif calBmi>=18.5 and calBmi<23:
        return '정상'
    else:
        return '저체중'

print(bmi(173,74))