# 예외 처리
# 에러가 발생했을 경우 어떻게 처리해야하는가?

# 에러가 나는 경우 (Syntex error 제외)
'''
print(15/0) #ZeroDivisionError: division by zero
'''
# 리스트 튜플 구조에서 인덱스가 없는 경우
'''
myList = [13,5,7,9,15] 
print(myList[15]) # IndexError: list index out of range
'''
# 파일 오픈 에러
'''
f = open('none.txt','r')
print(f.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'none.txt'
'''

try:
    4/0
except ZeroDivisionError as e:
    print(e,'ZeroDivisionError가 발생했습니다')

# 에러 무시
# pass 명령 이용
try:
    4/0
except ZeroDivisionError as e:
    pass

print('와우')

try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
'''
try:
    4/0
finally: #에러가 뜨더라도 강제로 실행
    print("뜨던 말던..")
'''
def myDiv(a,b):
    try:
        c = a/b

    except Exception as e:
        print('에러가 발생했습니다')

    else:
        return c

print(myDiv(5,'a'))