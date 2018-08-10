from urllib.request import urlopen
from bs4 import BeautifulSoup
html = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=154222&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2'
html = urlopen(html)
bs = BeautifulSoup(html,'html.parser')
'''
greenList = bs.find_all(class_="green")
redList = bs.find_all(class_="red")
text_id = bs.find(id="text")
for i in greenList:
    print(i.string)
    print('-' * 50)

for i in redList:
    print(i.string)
    print('-' * 50)

print('-'*50)
print(text_id)
'''
score_reple = bs.select('div.score_result > ul > li > div.score_reple > p')

for i in score_reple:
    print(i.string)