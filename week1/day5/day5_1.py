# 파일 읽기
# 파일에 관련된 함수 = 파일변수.함수(옵션)
# 파일변수.read() -> 문자열
# 파일변수.readline() -> 문자열
# 파일변수.readlines() -> 리스트
# 파일변수.write()
# 파일변수.write(data)

# with - 별도의 close가 필요없음.
# 들여쓰기 주의
with open('../data/Yesterday.txt','r',encoding='utf-8') as yesterday:
    readFile = yesterday.read()
    print(readFile)
print('-'*40)

with open('../data/Yesterday.txt','r',encoding='utf-8') as yesterday:
    readFile = yesterday.readline()
    print(readFile)
print('-'*40)

with open('../data/Yesterday.txt','r',encoding='utf-8') as yesterday:
    readFile = yesterday.readlines()

    for line in readFile:
        p = line.replace('\n','')
        print(p)


# with로 파일 쓰기
with open('../data/test1.txt','w',encoding='utf-8') as test:
    data = 'ㅏ핳하하ㅏㅏ하핳'
    test.write(data)

fruits = ['바나나','딸기','포도']
with open('../data/test2.txt','w',encoding='utf-8') as test:
    data = '과일들이다\n'
    test.write(data)
    for line in fruits:
        test.write(line+'\n')

# 외부 텍스트를 열어서 새로운 파일에 저장하기
with open('../data/Yesterday.txt','r',encoding='utf-8') as yesterday:
    readFile = yesterday.readlines()

    with open('../data/yesterday1.txt','w',encoding='utf-8') as t:
        for line in readFile:
            p = line.replace('\n','')
            t.write(p+'---\n')
# 퀴즈
with open('../data/Yesterday.txt','r',encoding='utf-8') as y:
    readFile = y.readline()
    with open('../data/result.txt','w',encoding='utf-8') as t:
        t.write(readFile)

# 기존 파일에 내용 추가하기
with open('../data/test1.txt','a',encoding='utf-8') as f:
    f.write('롯데마트 오픈\n')

# 퀴즈
with open('../data/gugu.txt','w',encoding='utf-8') as g:
    for i in range(2,10):
        for j in range(1,10):
            result = '%d X %d = %d \n' % (i,j,(i*j))
            g.write(result)