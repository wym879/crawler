from urllib import request
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库
import time


def mutilpage():
    for i in range(1,31):
        print('page:'+str(i))
        url = "https://www.chunyuyisheng.com/pc/doctors/0-0-0/?page="+str(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        page = request.Request(url, headers=headers)
        page_info = request.urlopen(page).read().decode('utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody

        # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
        soup = BeautifulSoup(page_info, 'html.parser')
        # print(soup.prettify())
        doctor_lists = soup.find_all('div', 'detail')
        for i in range(len(doctor_lists)):
            a = list(doctor_lists[i].descendants)
            plist = []
            name = ''.join(a[3].split())
            lab = ''.join(a[5].split())
            level = ''.join(a[7].split())
            hospital = ''.join(a[10].split())
            consult = a[15]
            rate = a[19]
            feild = a[21][3:]
            plist.extend((name, lab, level, hospital, consult, rate, feild))
            print(plist)
        time.sleep(1)


if __name__ =='__main__':
    mutilpage()