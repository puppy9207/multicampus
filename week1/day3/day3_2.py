# 집합(set)
# 자료값의 중복을 허용하지 않는다.
# {값1, 값2, ....}

# 집합 정의 1
# 집합이름 = set(리스트)
set1 = set([1,2,3,4,3,5,6,3])
print(set1)

# 집합 정의 2
# 집합이름 = set(문자열)
set2 = set('banana')
print(set2)

# 집합 정의 3
# 집합이름 = set(튜플)


# 집합 연산
# 합집합
# 문법1 : 집합1|집합2
# 문법2 : 집합1.union(집합2)
set1 = set(['a','b','c','d'])
set2 = set(['a','c','f','e'])

print(set1|set2)
print(set1.union(set2))

# 교집합
# 문법1 : 집합1 & 집합2
# 문법2 = 집합1.intersection(집합2)
set1 = set(['a','b','c','d'])
set2 = set(['a','c','f','e'])
print(set1&set2)
print(set1.intersection(set2))

# 차집합
# 문법1 = 집합1 - 집합2
# 문법2 = 집합1.difference(집합2)
print(set1-set2)
print(set1.difference(set2))

# 집합 요소 추가하기
# 집합이름.add(값)
set3 = set(['김씨','이씨','박씨','고씨'])
print(set3)
set3.add('강씨')
print(set3)

# 집합 요소 추가히기 2
set3 = set(['김씨','이씨','박씨','고씨'])
print(set3)
set3.update(['신씨','정씨'])
print(set3)

# 집합 요소 삭제
# 집합이름.remove(값)
set3 = set(['김씨','이씨','박씨','고씨'])
print(set3)
set3.remove('김씨')
print(set3)

# 집합 -> 리스트
set3 = set(['김씨','이씨','박씨','고씨'])
print(set3)
set_list = list(set3)
print(set_list)