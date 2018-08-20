import random
# 로또는 1~45까지의 번호
# 6개의 번호
# 작은순으로 정렬되어야함
# 5 게임
# 86% 신뢰구간에서 100~170이 정규분포 구간에 있음
# 합계가 100~170까지만 쓰자

# 2차원 배열, 1차원에는 6개의 번호 랜덤 입력
# 2차원은 5개

game = []
cnt2 = 0
while(True):
    # 초기화
    cnt1 = 0
    rotto = []

    while(True):
        check = random.randrange(1, 45) # 랜덤 숫자 생성
        rotto.append(check) # 숫자 입력
        rotto = list(set(rotto)) # 중복 제거
        if len(rotto) == 6: # 길이가 6일때만 다음 게임으로 넘어감
            break
        cnt1+=1
    # 합계가 100에서 170인것만 넣음
    if 100<=sum(rotto)<=170:
        rotto.sort()  # 정렬
        game.append(rotto)
        cnt2+=1
    else:
        pass

    if cnt2 == 5:
        break



for i in game:
    print(i)