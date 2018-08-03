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
    pass