#자료형
#정수, 실수, 문자열 - 단일 자료형
#리스트, 튜플, 딕셔너리, 집합

# 리스트(list)
# 정의 리스트이름 = [값1,값2,값3]
fruits = ['사과','바나나','수박','망고']
print('fruits 목록 : %s' % fruits)
# 리스트 인덱싱
print('fruits[0] : %s' % fruits[0])
print('fruits[-1] : %s' % fruits[-1])

#리스트 요소의 교체
fruits[0] = '자두'
print('fruits 목록 : %s' % fruits)

#리스트 전체의 길이
print('fruits 리스트 전체의 길이 %d' % len(fruits))

#리스트 요소의 부분 추출
a = [1,2,3,4,5]
print(a[0:2])
b = a[:2]
c = a[2:]
print(b)
print(c)

# 리스트 요소의 추가
# 리스트이름.append(요소값)
# 추가하는 곳은 마지막 위치에 추가한다.
print("-"*40)
fruits=["사과","망고","바나나","오렌지"]
fruits.append("복숭아")
print(fruits)

drama = []
print("드라마 리스트 : ", drama)
# data = input('드라마를 입력해주세요\n')
# drama.append(data)
print("드라마 리스트 : ", drama)

# 리스트 특정 위치에 요소 삽입
# 리스트 이름.insert(위치,요소값)
# 인덱스에서 지정한 위치에 요소 삽입
num = [22,35,15,25]
print("num : ",num)
num.insert(2,31)
print("num : ",num)

# 리스트 요소 삭제
# remove(삭제할 요소 값) 함수
a = [1,5,4,3,1,5]
a.remove(4)
print(a)

# 리스트 요소 끄집어내기
# pop 함수 기본은 마지막 위치를 뽑아낸다
# 리턴값이 있다! 삭제한 값의 인덱스값을 리턴한다
a = [1,5,4,3,1,5]
print(a.pop(1))
print(a)

# 리스트 요소 삭제
# del 리스트이름[인덱스]
foods = ['라면','치킨','돈가스']
print('푸드 리스트 :',foods)
del foods[0]
print('푸드 리스트 :',foods)

# 리스트끼리 합하기
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a+list_b)

# 리스트 곱하기 - 리스트 요소 반복하기
list_c = ["하이","안녕","니하오"]
print(list_c*3)