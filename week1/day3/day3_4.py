# 짝수홀수판별기
'''
in_data = int(input('숫자를 입력하세요\n'))

if in_data%2 == 1:
    print("홀수입니다")
elif in_data%2 ==0:
    print("짝수입니다")
else:
    print("정수를 입력해주세요")
'''
# BMI 값에 따라 출력
'''
height = int(input('키를 입력하세요 \n'))
weight = int(input('체중을 입력하세요 \n'))
# bmi = w(kg)/h(m)제곱
bmi = weight/((height/100)**2)
print(bmi)
if bmi>35:
    print('고도비만')
elif bmi>=30 and bmi<35:
    print('중증도 비만')
elif bmi>=25 and bmi<30:
    print('경도비만')
elif bmi>=23 and bmi<25:
    print('정상')
else:
    print('저체중')
'''
a = -421.1513545465
print('a의 값은 %+.2f' % a)
# 내 띠 찾기
year = int(input('태어난 년도를 말씀해주세요'))
print(year%12)
zodiac = {0:'원숭이',1:'닭',2:'개',3:'돼지',4:'쥐',5:'소',6:'범',7:'토끼',
          8:'용',9:'뱀',10:'말',11:'양'}
print(zodiac[year%12])