# 반복문 while
# while 조건:
#    실행명령

# 무한 루프
while True:
    print('python')
    break

# False일때 탈출한다!

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print('나무 넘어간다~~')

num = 10
while num>0 :
    print(num)
    num -= 1

# 퀴즈 별개수 많아지게하기~
aster = '*'
num = 1
while num<11:
    print(aster*num)
    num+=1

# 역으로
aster = '*'
num = 10
while num>0:
    print(aster*num)
    num-=1

# 1부터 50까지 합
num = 1
sum = 0
while num<=50:
    sum += num
    num += 1
    print(sum)

# 구구단
gugu = int(input('정수를 입력하세요\n'))
count = 1
while count <= 9:
    print('%d * %d = %d' % (gugu,count,(gugu*count)))
    count+=1

# Break
# 보통 무한 루프를 걸어놓고 빠져나가게 할 때 break사용
# 그리고 탈출할 조건제어문을 쓰고 조건이 맞으면 break
while True:
    ans = input('아무값이나 입력하세요 종료는 x입니다')
    #탈출조건
    if ans == 'x':
        break
print('입력종료')

# 퀴즈
# 리스트 요소 추가
myList = []
while True:
    ans = input('입력할 값을 넣어주세요')
    if ans == 'x':
        break
    myList.append(ans)
print(myList)