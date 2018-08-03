# 가변인자
# def 함수명(*인자명):
#   명령문
#   return
'''
def print_n(*value):
    for i in value:
        print(i)

print_n('python')
print_n('aaaa','asdsdas')
print_n(100,200,300,400)
'''
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i

    return sum

print(sum_many(2,5,7,2,4))

# 전역변수 선언
# 함수 안의 global변수는
# 함수 블록 밖에서도 같은 변수일때
# 영향을 끼친다.

print("-"*50)
a = 5
print(a)
def test():
    global a
    a= 10
    print(a)

test()
print(a)

# 람다 함수 : 익명함수
# 임시적인 함수
f = lambda x,y : x+y
print(f(4,5))
