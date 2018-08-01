money = 0

if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print('='*20,'끝')

# 다른 언어에서는 else if 를 사용하는데
# 파이썬에서는 elif로 사용한다.

money = 3000
if money>=3000:
    print("택시타자.. 듭다")
elif money<3000 and money>=2000:
    print("버스라도 탑시다!")
elif money<2000 and money>=1000:
    print("아이스크림이라도... 사먹자..")
else:
    print("돈없으면 쪄죽어야지")

# in 연산자
# 결과값이 True or False
# item1 in Group(문자열,리스트,튜플 ...)

# 문자가 문자열에 있는가?
print('a' in 'banana')
print('a' in 'python')

# 아이템이 리스트에 있는가?
list1= [1,2,3,4,5,6,7]
print(8 in list1)

# 아이템이 튜플 안에 있는가?
tuple1 = (1,2,5,8,4,3,5)
print(2 in tuple1)

# 아이템(요소)이 집합 안에 있는가?
userName= {'홍길동','로미오','줄리엣'}
print('홍길동' in userName)

# not in 연산자
# 결과값이 True / False
# Item not in Group
# 아이템이 그룹안에 없다면 True
# 위에서 not만 붙여주면 된다.
userName= {'홍길동','로미오','줄리엣'}
print('홍길동' not in userName)

# if문에서 사용해보기
myList = ['바나나','사과','딸기']
if '바나나' in myList:
    print('바나나가 안에 있음')
else:
    print('바나나가 안에 없음')

# 퀴즈
# 학점별 등급
score = float(input('당신의 학점을 입력하세요'))
if score>4.5:
    print('수업시간에 딴짓하고 문제 안읽는애들')
elif score==4.5:
    print('신')
elif score<4.5 and score>=4.2:
    print('교수님의 사랑')
elif score<4.2 and score>=3.5:
    print('현 체제의 수호자')
elif score<3.5 and score>=2.8:
    print('일반인')
elif score<2.8 and score>=2.3:
    print('일탈을 꿈꾸는 소시민')
else:
    print('시대를 앞서가는 혁명의 씨앗')