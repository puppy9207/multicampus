# 자료 구조 변환 Casting
# 문자열 -> 리스트
# 문자열변수.split()
myStr = '피자 치킨 족발 보쌈 삼계탕 탕수육 짜장면'
myList = myStr.split()
print(myList)

myStr = '피자ㅁ치킨ㅁ족발ㅁ보쌈'
myList = myStr.split('ㅁ')
print(myList)

# 리스트 -> 문자열
# str(리스트 이름)
myList = ['김','이','박']
print(str(myList))
# 김이박 <- 이렇게 들어가는게 아니라 ['김','이','박'] <- 이런식으로 괄호와 인용구호도 같이 들어간다.


# 리스트 -> 문자열 2
# '구분자'.join(리스트)
myList = ['김','이','박']
print(myList,type(myList))
result = ' '.join(myList)
print(result, type(result))

# 문자열 -> 리스트
# (공백포함) 모든 글자를 모두 분리해서 넣음
myStr = '안녕 무궁화 미나리'
print(myStr,type(myStr))
myList = list(myStr)
print(myList,type(myList))

# 리스트 요소 정렬하기
# 리스트이름.sort()
# 리스트이름.reverse()
# 조건 : 리스트 요소의 데이타형이 같아야한다.
myNum = [1,5,25,3,57,111,102]
print(myNum)
myNum.sort()
print(myNum)
myNum.reverse()
print(myNum)

# 리스트 위치 반환하기
food = ['닭발','보쌈','치킨','샌드위치','파전']
print(food.index('치킨'))

# 리스트 안의 x의 개수 파악하기
num = [1,3,5,1,1,5,7,6,5,4]
print(num.count(1))



