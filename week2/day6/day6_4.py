# CSV 파일 입출력

import pandas as pd
import csv # csv 모듈 사용
f = open('../data/test.csv','r',encoding='utf-8-sig')
csv_data = csv.reader(f)
lst_data = []
for line in csv_data:
    lst_data.append(line)
    print(line)

print(lst_data)
lst_data = pd.DataFrame(data=lst_data[1:],columns=lst_data[0])
print(lst_data)
f.close()
'''
# with
with open('../data/test.csv,','r',encoding='utf-8-sig') as f:
    csv_data = csv.reader(f)
    for line in csv_data:
        lst_data.append(line)
'''
# 리스트 -> csv 파일로 출력
f = open('../data/output.csv','a',encoding='utf-8-sig')
wr = csv.writer(f)
wr.writerow([1,'2014315006'])
wr.writerow([2,26])
wr.writerow([3,'생명화학공학과'])
wr.writerow([4,'소진권'])
wr.writerow([5,'남'])
f.close()