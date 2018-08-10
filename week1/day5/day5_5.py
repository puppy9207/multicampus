# 함수의 종류
# - 내장함수
#   : import 없이
#     len(), type() 등등
#   : import 해야만 사용 가능한 함수
# - 사용자 정의 함수

# abs(숫자) : 절대값 추출
print(abs(5))
print(abs(-5))
print(abs(5.5))
print(abs(-5.5))

# divmod(n1,n2) 몫과 나머지를 함께 리턴
print(divmod(5,4)) # 튜플 형태로 리턴
print(divmod(7,3))
print(divmod(6,3))

# eval(data) - data를 계산식으로 변경해서 계산 결과를 리턴

data = 'int(1.552)'
print(eval(data)) # 1

# len() 길이 구할때
data = [1,2,3,4,5,6]
print(len(data)) #6

# max(리스트,튜플), min() 각각 리스트의 최댓값, 최솟값 리턴
data = [1,8,15,6,484,21]
print(max(data)) # 484
print(min(data)) # 1

# enumerate(리스트, 시작번호) 색인을 부여한다
myList = ['apple','banana','caramel','diamond']
for index, value in enumerate(myList,1):
    print(index,value)

# map(정의된함수,데이타(리스트,튜플))
# 출력할때 리스트 형식으로 보고싶다면 list를 씌워야한다
data1 = list(map(lambda x:x**2,[1,2,5,6]))

print(data1)

# isalpha, isdigit -> 알파는 문자가 들어가는지 판단, 디짓은 숫자가 들어가는지 판단
str1 = '가나다'
str2 = '11231'
str3 = '가123'
print(str1.isalpha())
print(str1.isdigit())
print('-'*40)
print(str2.isalpha())
print(str2.isdigit())
print('-'*40)
print(str3.isalpha())
print(str3.isdigit())

# filter 리스트 요소 중에서 함수 조건에 맞는 것만 필터링
# 짝수값만 출력
data2 = list(filter(lambda x:x%2==0 ,[1,2,3,4,5]))
print(data2)

# zip 같은 인덱스 값으로 짝짓는다.
actor = ['정우성','김태희','톰크루즈']
gender = ['남','여','남']
for i,j in zip(actor,gender):
    print(i+'-'+j)
print(list(zip(actor,gender)))
# 리스트 안에 튜플 형식으로 저장

# 퀴즈
aList = [50,15,56,22]
bList = [81,21,35,66]

cList = aList+bList
print('max = %d min = %d' %(max(cList),min(cList)))

in_v = input('뭐든 입력해보세요')
result_list = []

def list_in(v):
    if str(v).isdigit():
        result_list.append(int(v))
    else:
        print('숫자가 아닙니다 다시 출력해주세요')

list_in(in_v)
print(result_list)

h = 'hellopythonworld'
print(h[5:11])
