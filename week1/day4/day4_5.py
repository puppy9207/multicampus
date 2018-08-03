# 파일 읽기
'''
file = open("data/yesterday.txt",'r',encoding='utf-8')
data = file.read()
print(data)
print(type(data))
myList = data.split()

for i in myList:
    print(i)
print(len(myList))
file.close()
'''
# 여태까지 한걸 함수로 만들자

def openTxt(root):
    file = open(root,'r',encoding='utf-8')
    data = file.read() # 다 읽어옴
    myList = data.split()
    file.close()
    return len(myList)
print(openTxt('data/yesterday.txt'))

# 파일 읽기
# 위의 read는 모든 데이터를 문자열로 처리한다
# readline
f = open('data/Yesterday.txt','r')
data2 = f.readline() # 한줄만 읽어옴
print(data2)
f.close()

f = open('data/mytxt.txt','r',encoding='utf-8')
data3 = f.readlines() #리스트 형태로 다 읽어옴
print(data3)
for i in data3:
    print(i,end='')
f.close()

# 샘플 텍스트파일의 줄수가 몇개인지 출력하여라
def openLine(root):
    f = open(root,'r',encoding='utf-8')
    data = f.readlines()
    f.close()
    return len(data)

print('\n','-'*40)
print(openLine('data/mytxt.txt'))

def openTxtAndSumMul(root):
    f = open(root,'r',encoding='utf-8')
    data = f.readlines()
    f.close()
    sum1 = 0
    count = 0
    for i in data:
        sum1 += int(i)
        count += 1
    average = sum1 / len(data)
    print('합',sum1)
    print('평균',average)

    # 이하 결과 쓰기
    r = open('data/result.text','w',encoding='utf-8')
    cntResult = '데이터 수는 %d 이다\n' % count
    r.write(cntResult)
    sumResult = '합은 %d 이다 \n' % sum1
    r.write(sumResult)
    avgResult = '평균은 %d 이다.' % average
    r.write(avgResult)
    r.close()

openTxtAndSumMul('data/number.txt')

def charCount(url):
    f = open(url,'r',encoding='utf-8')
    data = f.readlines()
    f.close()
    count = 0
    for i in data:
        for j in i:
            if j !='\n':
                count +=1

    return count

print(charCount('data/number.txt'))
# 이하 파일 쓰기
'''
f = open('data/test1.txt','w',encoding='utf-8')
for i in range(1,11):
    data ='%d번째 줄입니다. \n' % i
    f.write(data)
f.close()

myList = ['바나나','딸기','생크림','케이크','쥬스','오렌지']
f = open('data/test2.txt','w',encoding='utf-8')
for i in myList:
    data = str(i)+'\n'
    f.write(data)
f.close()
'''