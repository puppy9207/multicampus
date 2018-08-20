from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
start_time = time.time()

html = urlopen("http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo=820")

soup = BeautifulSoup(html, "html.parser")
h3 = soup.find("h3",{"class":"result_title"})
hoi = h3.strong.string
print(hoi,"회")
number = []
p = soup.find("p",{"class":"number"})
imgs = p.find_all("img")
for i in imgs:
    alt = i["alt"]
    number.append(int(alt))

bonus = number.pop() #마지막 값을 뽑아냄
print(number,bonus)
print("--- %s seconds ---" %(time.time() - start_time))