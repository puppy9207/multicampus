#기본 자료형
#숫자형(정수, 실수), 문자열, 불린(true,false)

print(10>0)
print(True != True)

#관계 연산자
#> , < , >=, <=, ==, !-

print(10 == 0)

#Casting 자료형 변환. 자료형을 변경하는 기능
#숫자 -> 문자, 문자 -> 숫자, 실수 -> 정수, 정수 -> 실수

#1. 숫자 -> 문자
print(1) #정수형 타입
print(type(1))
print(str(1))
print(type(str(1)))

print('-'*30)
#2.1 문자 -> 숫자(정수)
print('12')
print(type('12'))
print(int('12'))
print(type(int('12')))

print('-'*30)
#2.2 문자 -> 숫자(실수)
print('1.25')
print(type('1.25'))
print(float('1.25'))
print(type(float('1.25')))

print('-'*30)
#3. 정수 -> 실수
print(25)
print(type(25))
print(float(25))
print(type(float(25)))

#여태까지는 출력문
#입력문 배우기
#input('숫자를 입력하세요 \n')

'''
변수
- 값을 저장할 수 있는 공간

- 변수 이름 지정시 규칙
 : 첫글자는 영문자
 : 숫자, 영문자, _(언더바) 가능
 : 키워드 사용 불가 (print, input, int 등등)
 
- 변수 이름 지정 스타일
 카멜 스타일 : 단어별로 대문자 첫글자
 ex) numberOneValue
 스네이크 스타일 : 단어별로 언더바
 ex) number_one_value
 
'''

#inData = input('뭔가를 입력하세요')
#print(inData)
# 입력문에서 입력받은 값은 문자형으로만 들어간다.
print('\n'*5)

#입력받은 2개의 숫자를 더하기
num1 = input('숫자 1번\n')
num2 = input('숫자 2번\n')
print('덧셈',int(num1)+int(num2))
print('뺄셈',int(num1)-int(num2))
print('곱셈',int(num1)*int(num2))
print('나눗셈',int(num1)/int(num2))