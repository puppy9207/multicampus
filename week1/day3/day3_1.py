# 딕셔너리 자료형
# java의 hash
# 딕셔너리는 순서가 없다.
# {Key : Value}

dict1 = {'a' : 'aboard', 'b' : 'banana', 'c' : 'camel'}
print(dict1)
dict2 = {'a' : 'aboard', 'b' : 'boo', 'c' : 'caramel'}
print(dict2)

# 딕셔너리 요소 호출
# 딕셔너링이름 [키값]
print('dict1[\'a\'] :',dict1['a'])

# 딕셔너리 추가
dict1 = {'a' : 'aboard', 'b' : 'banana', 'c' : 'camel'}
print('dict1 = ', dict1)
dict1['d'] = 'drive'
print('dict1 = ', dict1)

# 딕셔너리 삭제
# del 딕셔너리 이름[키값]
dict1 = {'a' : 'aboard', 'b' : 'banana', 'c' : 'camel'}
print('dict1 = ', dict1)
del dict1['a']
print('dict1 = ', dict1)

# 딕셔너리 요소 모두 삭제하기
# 딕셔너리이름.clear
dict1 = {'a' : 'aboard', 'b' : 'banana', 'c' : 'camel'}
print('dict1 = ', dict1)
dict1.clear()
print('dict1 = ', dict1)

# 딕셔너리 요소중에서 키값, 밸류값만 모아서 재정의하기
dict3 = {'name':'고주원','address':'서울시 중랑구','tel':'010-3381-9207'}
print('dict3 = ', dict3)
print(type(dict3))
print(dict3.keys())
keys_list = dict3.keys()
values_list = dict3.values()

# 딕셔너리 -> 문자열
dict3 = {'name':'고주원','address':'서울시 중랑구','tel':'010-3381-9207'}
print(str(dict3))
myStr = ' '.join(dict3)
print(myStr) #키값만 들어옴

# 딕셔너리 -> 리스트
dict3 = {'name':'고주원','address':'서울시 중랑구','tel':'010-3381-9207'}
print(dict3)
dict_list = list(dict3)
dict_value_list = list(values_list)
print(dict_list) #키값만 들어옴
print(dict_value_list)

# 딕셔너리 -> 튜플
# 딕셔너리 -> 리스트
dict3 = {'name':'고주원','address':'서울시 중랑구','tel':'010-3381-9207'}
print(dict3)
dict_list = tuple(dict3)
print(dict_list)

# 퀴즈
car_dict = {'spark':'chevorlet','ray':'kia','sm5':'renausamsung','stinger':'kia'}
print(len(car_dict))