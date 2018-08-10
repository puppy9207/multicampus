# for문을 이용하여 리스트에 정의된 아이템을
# csv 파일로 저장하기
# 2차원 리스트로 정의
import csv
fruitList = [[1,'사과','배'],[2,'토마토','방울토마토'],[3,'바나나','귤']]
f = open('../data/output_f.csv','w',encoding='cp949',newline='')
wr = csv.writer(f)
for line in fruitList:
    wr.writerow(line)
f.close()
'''
fo = open('../data/output_f.csv','r',encoding='cp949')
wo = csv.reader(fo)
for line in wo:
    print(line)
'''
pop = open('../data/population.csv','r',encoding='utf-8-sig')
population = csv.reader(pop)
state = []
ingu = []
for line in population:
    state.append(line[0])
    ingu.append(line[1])

print(ingu[1])
ingu1 = []
for i in ingu:
    ingu1.append(i.replace(',',''))

print(int(ingu1[1]))
del ingu1[0]
print(ingu1)
result = 0
for i in ingu1:
    result+=int(i)

print(result)