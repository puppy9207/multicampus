# 문자열 함수
# 문자열변수.count(찾을 문자)

myStr = 'Python String Function Well Made String'
print(myStr)
print('myStr 문자열은 {}'.format(myStr))
print('myStr 문자열은 %s' % (myStr))
print(myStr.count("String")) #.count는 리턴값이 정수형이다.

#문자열변수.find(찾을 문자)
print(myStr.find("String"))
# - 위치값을 반환한다
# - 찾을 문자가 여러개일 경우 가장 앞에 있는 값을 리턴한다.
# - 리턴값은 정수형
# - 반환값이 -1이라면 찾는 문자가 없다.

# 문자열 삽입 join
a = ','
print(a.join('abcd'))
# 문자열 각각에 a(문자열이나 문자열 변수) 변수를 삽입한다.

# 대문자를 소문자로 바꾸기 .lower
al = 'HI HELLO'
print(al.lower())

# 소문자를 대문자로 바꾸기 .upper
al = 'hi hello'
print(al.upper())
print(al)

#양쪽 공백 지우기(strip)
b = ' hi  '
print(a.strip())
#왼쪽 공백 지우기(lstrip) 오른쪽 공백 지우기(rstrip)

#문자열 바꾸기(.replace(찾는문자,변경할문자))
a = "Life is too short, You need to Java"
print(a.replace(" ",""))
print(a)

#퀴즈 1
flower = "좋아하는 꽃 - 장미"
print(flower)
print(flower.replace("장미","백합"))
print(flower.replace("꽃","flower"))

#퀴즈 2
example = "Let thy speech be short, comprehending much in few words."
print("첫번째 t의 위치 : %d" % example.find("t"))
print("첫번째 m의 위치 : %d" % example.find("m"))
print("s의 개수 : %d" % example.count("s"))
print("=으로 연결\n %s" % "=".join(example))
print("대문자로 연결 \n %s" % example.upper())