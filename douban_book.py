import urllib.request
from bs4 import BeautifulSoup
def get_html(url):
    web=urllib.request.urlopen(url)
    soup=BeautifulSoup(web,"html.parser")
    data=soup.find("div",id="wrapper")
    return data
def get_all(data):
    data=data.find_all("table")
    for link in data:
        name=link.find("div",class_="pl2").find("a").get_text().replace(' ','').replace('\n','')
        author=link.find("p",class_="pl").get_text().split('/')[0].replace(' ','')
        score=link.find("span",class_="rating_nums").get_text().replace(' ','')
        peoplenum=link.find("span",class_="pl").get_text().replace(' ','').replace('(','').replace(')','').replace('\n','')
        try:
            remark=link.find("p",class_="quote").get_text().replace(' ','').replace('\n','')
        except:
            remark='暂无评价'
        with open('/home/wei/桌面/book.txt','a+', encoding='UTF-8') as f:
            f.write(name+' '+author+' '+score+' '+peoplenum+' '+remark+'\r\n')
if __name__ == '__main__':
    url='https://book.douban.com/top250?start='
    with open('/home/wei/桌面/book.txt','a+', encoding='UTF-8') as f:
        f.write('书籍名称 '+'作者 '+'评分 '+'评价人数 '+'评论 '+'\r\n')
    for i in range(10):
        url1=url+str(i*25)
        get_all(get_html(url1))