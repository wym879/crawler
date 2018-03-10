from urllib import request
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库

# 构造头文件，模拟浏览器访问
url = "https://www.chunyuyisheng.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')
details = soup.find_all('div','detail')
for i in range(len(details)):
    a = list(details[i].descendants)
    plist = []
    name = ''.join(a[6].split())
    lab = ''.join(a[9].split())
    level = ''.join(a[12].split())
    hospital = ''.join(a[19].split())
    consult = str(a[27])
    rate = str(a[32])
    feild = a[36][3:]
    plist.extend((name, lab, level, hospital, consult, rate, feild))
    print(plist)