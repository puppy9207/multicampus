'''
연산자 종류
 -문자열 연산자 : +, *
 -산술 연산자 : +,-,*,/,//,%,**
 -관계 연산자 : ==, <=, >=, >, <
 -대입 연산자 : +=, -=, *= , /=, (++,-- 증감연산자는 없음)
'''
a = 10
b = 10
b += a
print(b)

# .format {}
print('{a1} {b}'.format(a1=12,b=33))
a= 10
b= 5
print('a = {}, b = {}'.format(a,b))
# 퀴즈
'''
in_a = int(input('첫번째 숫자\n'))
in_b = int(input('두번째 숫자\n'))
print(in_a,'+',in_b,'=','{}'.format(in_a+in_b))
print(in_a,'-',in_b,'=','{}'.format(in_a-in_b))
print(in_a,'*',in_b,'=','{}'.format(in_a*in_b))
print(in_a,'/',in_b,'=','{}'.format(in_a/in_b))
'''
#포맷팅 % 이용
# %d 정수 %f 실수 %s 문자열 %c 문자
print("%0.3f %0.3f" % (0.55555,0.636363))

#퀴즈
# in_a = int(input('첫번째 숫자\n'))
# in_b = int(input('두번째 숫자\n'))
# print('%d + %d = %d' % (in_a,in_b,(in_a+in_b)))
# print('%d - %d = %d' % (in_a,in_b,(in_a-in_b)))
# print('%d * %d = %d' % (in_a,in_b,(in_a*in_b)))
# print('%d / %d = %0.3f' % (in_a,in_b,(in_a/in_b)))

#문자열 인덱싱
python = 'Life is too short, You need Python'
print(python[0:5])

#아스키 코드 변환기
def ascii(string_in):
    if isinstance(string_in,str):
        count = 0
        result = []
        for i in string_in:
            result.append(str(ord(i)))
            count += 1
        return "&"+"&".join(result)
    else:
        return 'wrong type'

print(ascii(python))
#문자열 슬라이싱 - 부분 추출
strTest = 'Life is too short, You need Python'
print(strTest[:5],strTest[-6:])