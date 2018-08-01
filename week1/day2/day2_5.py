# 다중 리스트
# 2차원 리스트
myList = [[2,3],[4,5],[7,8]]

# 2차원 리스트 인덱싱
# myList에서 3을 찾고 싶으면?
print(myList[0][1])

# 2차원 리스트 정의
# 위의 myList 같이 정의하는 방법이 있고
# 1차원 리스트로 구성된것을 -> 2차원으로 조합하는 방법이 있다.
userName= ['홍길동','고주원','정예진']
userId=['hong123','puppy9207','jung123']
userAge = [29,24,24]
print(userName,userId,userAge)
userList = [userName,userId,userAge]
print(userList)
#고주원을 찍어보자
print(userList[0][1])
#jung123을 찍어보자
print(userList[1][2])
#29를 찍어보자
print(userList[2][0])

#퀴즈
kor = [55,66,34,60]
math = [78,90,45,88]
eng = [56,98,78,90]

grade = [kor,math,eng]

print('kor 총점 (%d), 평균 (%d)' % (sum(kor),sum(kor)/len(kor)))
print('math 총점 (%d), 평균 (%d)' % (sum(math),sum(math)/len(math)))
print('eng 총점 (%d), 평균 (%d)' % (sum(eng),sum(eng)/len(eng)))
