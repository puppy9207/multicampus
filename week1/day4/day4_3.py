# 

# 퀴즈1
'''
  입력받은 
  값 n으로 1~n 까지의 
  합계찍기에 관련된 함수를 정의하고 
  결과를 출력한다.

  10을 입력받았다면?

  1~10 의 합 : ?
'''

n= int(input('정수를 입력하세요'))

def sumEvery(n1):
    result = 0
    for i in range(1,n1+1):
        result += i

    return result

print(sumEvery(n))


# 퀴즈2
'''
3개의 인자 값을 입력받은 후 
첫번째 인자 값에 따라 사칙 연산하기 

첫번째 인자값이 c1 이라면?
cal(c1,2,3) - 더한다
cal(c2,2,3) - 뺀다 
cal(c3,2,3) - 곱한다
cal(c4,2,3) - 나눈다 

result = 5

'''

def cal(cal1,num1,num2):
    result = 0
    if cal1 == 'c1':
        result = num1+num2
        return '더한다',result
    elif cal1 == 'c2':
        result = num1-num2
        return '뺀다',result
    elif cal1 == 'c3':
        result = num1*num2
        return '곱한다',result
    elif cal1 == 'c4':
        result = num1/num2
        return '나눈다',result
    else:
        return '입력오류'

print(cal('c3',3,5))
