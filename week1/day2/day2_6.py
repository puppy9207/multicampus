# 튜플
# 튜플은 () 소괄호로 생성한다
# 튜플은 값을 삭제, 변경할 수 없다. 추가와 읽기만 가능

# 튜플 구조 정의 1
t1 = ('도','레','미','파','솔')
print(t1)

# 튜플 구조 정의 2
t2 = 1,2,3,4,5,6,7
print(type(t2))

# 튜플 인덱싱
# 튜플이름[위치번호] 0번부터 시작
t1 = ('도','레','미','파','솔')
print(t1)
print(t1[0])
print(t1[-1])
print(t1[0:2])
# 리스트의 인덱싱 방식과 똑같다.
# 삭제, 변경은 불가능
# 추가는 가능
myTuple = (100,'강아지','지렁이')
print(myTuple)
print('myTuple[0] = ',myTuple[0])
# myTuple[0] = 210 # error / TypeError: 'tuple' object does not support item assignment

# 튜플 함수 적용
# count
print(myTuple.count(100)) #가능
# 튜플은 sort가 불가능하다.
# print(myTuple.sort())
# AttributeError: 'tuple' object has no attribute 'sort'
# 튜플클래스에 sort라는 함수가 아예 없음

# len(튜플이름)
print(len(myTuple))

# index 찾기
print(myTuple.index('강아지'))

# 자료구조 변환
# 문자열 => 튜플
myStr = 'Python'
print(myStr,type(myStr))
myTuple = tuple(myStr)
print(myTuple,type(tuple))

# 리스트 -> 튜플
myList = ['수학','과학','영어']
print(myList,type(myList))
myTuple = tuple(myList)
print(myTuple,type(myTuple))

# 튜플 -> 리스트
myTuple = ('가','나','다')
print(myTuple,type(myTuple))
myList = list(myTuple)
print(myList,type(myList))

# 퀴즈
animals = ('강아지','토끼','돼지','곰')
animals += ('호랑이',)
print(animals)
print(animals[0:4])
animalList = list(animals)
print(animalList)