# continue는 반복문에서
# 특정 조건문이 있을때 해당 반복구간만
# 무시하고 다음 반복을 진행하게 할때 사용

a = 0
while a<10:
    a += 1
    if a==5:
        continue
    print(a,end=' ')

myList = range(0,10)
print(myList)

# range 함수를 쓰면 해당 숫자만큼 반복하는 반복문으로 사용가능
for i in range(0,10):
    print(i)
    print('hello')

# 파이썬의 for문의 특징은 range 부분에 리스트 형태의 변수를 넣으면
# 리스트 안에 있는 모든것들을 반복한다.

myList = ['a','b','c','d','e']
for i in myList:
    print(i)

# 다만 이런 리스트 형식으로 반복을 하면 다른 언어와 달리
# 카운트에 대한 변수를 따로 만들어야 하는 번거로움도 있다.

# 리스트에서 최대값 출력
myList = [1,5,3,7,8,9,55,12,64,81,2]
result = myList[0] #1
for i in myList:
    if result<i :
        result = i
print('최대값 = ', result)

# 중첩 for문
for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" % (i,j,(i*j)))