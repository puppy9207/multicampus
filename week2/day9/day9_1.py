from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
import csv
def get_html(i):
    html = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=154222&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%d' % i
    html = urlopen(html)
    return html


def croll_movie(html):
    try:
        bs = BeautifulSoup(html, 'html.parser')
        score_reple = bs.select('div.score_result > ul > li > div.score_reple > p')
        score = bs.select('div.score_result > ul > li > div.star_score > em')
    except Exception as e:
        return False

    return score_reple

def except_span(i):
    if i.string == None:
        a = str(i).replace("<p><span class=\"ico_viewer\">관람객</span>", "")
        a = a.replace("</p>", "")
        return [a,1]
    else:
        return [i.string,0]

def write_csv(an):
    with open('../data/movie.csv','a',encoding='utf-8-sig',newline='') as cs:
        wr = csv.writer(cs)
        for i in an:
            wr.writerow(i)

for l in range(1,1659):
    result = []
    html = get_html(l)
    a = croll_movie(html)
    for k in a:
        result.append(except_span(k))
    t1 = threading.Thread(target=write_csv, args=(result,))
    t1.start()
    print(l)






