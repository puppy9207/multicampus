# 시간과 관련된 모듈 임포트
import datetime

# 시간 전체에 관련된 변수 설정
# 현재 년도,월,일 시간이 저장된다.
now = datetime.datetime.now()
print(now)

# 현재 년도만 추출
print(now.year)

# 퀴즈
print('현재 년도는 %d년 %d월 %d일입니다. \n 현재시간은 (%d)시 (%d)분입니다' % (now.year,now.month,now.day,now.hour,now.minute))

# 퀴즈2
now = datetime.datetime.now()
hour = datetime.datetime.now().hour
if hour<13:
    print('현재 시간은 오전 %d시 %d분 입니다.' % (hour,now.minute))
else:
    hour = hour-12
    print('현재 시간은 오후 %d시 %d분 입니다.' % (hour,now.minute))

# weekday = 0~6 리턴 0 = 월요일
set_weekday = {0:'월요일',1:'화요일',2:'수요일',3:'목요일',4:'금요일',5:'토요일',6:'일요일'}
weekday = set_weekday[now.weekday()]

print('%d년 %d월 %d일 %s'%(now.year,now.month,now.day,weekday))