from urllib import request
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库
import time
import pickle
from urllib import error


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
        time.sleep(0.3)  # todo: 如何使用ip代理设置


def getComment():
    # 测试第一页的url获取
    data_store = []
    for i in range(1,31):
        url = "https://www.chunyuyisheng.com/pc/doctors/0-0-0/?page=" + str(i)
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        page = request.Request(url, headers=headers)
        page_info = request.urlopen(page).read().decode('utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody

        # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
        soup = BeautifulSoup(page_info, 'html.parser')
        details_url = soup.find_all('a', 'name-wrap')
        doctor_lists = soup.find_all('div', 'detail')
        # print(len(details_url))
        new_urls = []
        names = []
        for i in range(len(details_url)):
            new_urls.append("https://www.chunyuyisheng.com/" + details_url[i].get('href'))
            raw_name = list(doctor_lists[i].descendants)
            name = ''.join(raw_name[3].split())
            names.append(name)
        for i in range(len(new_urls)):
            try:
                comment = receiveTag(new_urls[i])
                print(names[i],comment)
                data_store.append((names[i],comment))
                time.sleep(1)
            except error.HTTPError as e:
                print('wrong page:', new_urls[i])
    with open("data.pk", 'wb') as f:
        pickle.dump(data_store, f)

def receiveTag(current_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(current_url, headers=headers)
    page_info = request.urlopen(page).read().decode('utf-8')
    soup = BeautifulSoup(page_info, 'html.parser')
    comments = soup.find_all('li', 'tag-item tag-item-dead')
    comment_list = []
    for i in range(len(comments)):
        # print('num:',num)
        element = list(comments[i].children)
        tag = ''.join(element[0].split())
        tag_num = str(element[1].string)
        current = tag+tag_num
        # print(current)
        comment_list.append(current)
    return comment_list


def readData():
    with open('data.pk','rb') as f:
        result = pickle.load(f)
    for i in result:
        print(i)

def getIPs():
    pass

if __name__ =='__main__':
    #getComment()
    #print('存储完成')
    #print('开始打印')
    #readData()
    mutilpage()