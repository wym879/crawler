import io
import sys
import urllib.request
from bs4 import BeautifulSoup
#获取网页
def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/60.0.3112.101 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    html=res.read()
    soup=BeautifulSoup(html,'html.parser')
    data = soup.find("ol").find_all("li")
    return data
def get_all(data):
    for info in data:
        names = info.find("span")
        name = names.get_text()
        scores = info.find_all("span",{"class":"rating_num"})
        score = scores[0].get_text()
        nums=info.find("div",class_="star").find_next().find_next().find_next().find_next().get_text()
        with open('/home/wei/桌面/movie.txt','a+', encoding='UTF-8') as f:
            f.write(name+' '+score+' '+nums+'\r\n')
if __name__ == '__main__':
    url='https://movie.douban.com/top250?start='
    with open('/home/wei/桌面/movie.txt','a+', encoding='UTF-8') as f:
        f.write('电影名称'+' '+'评分'+' '+'评价人数'+'\r\n')
    for i in range(10):
        url1=url+str(i*25)+'&filter='
        get_all(get_html(url1))