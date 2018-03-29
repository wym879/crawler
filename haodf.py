#  按专科 —->采集：疾病分类（url）
from urllib import request
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


def getDepartmentUrl():
    departmentInfo = []
    url = 'http://www.haodf.com/keshi/list.htm'
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read()
    soup = BeautifulSoup(page_info,'html.parser')
    detail_info = soup.find_all('a', 'black_link')
    for i in detail_info:
        name = i.get_text()
        url = i.get('href').split('.')[0]
        temp = {}
        temp['name'] = name
        temp['url'] = url
        departmentInfo.append(temp)
    return departmentInfo


def url_transfer(department_url):
    # transfer department_url(:/keshi/1010000) into url with page numbers
    department_url = 'http://haoping.haodf.com' + department_url + '/daifu_all.htm'
    print(department_url)
    page = request.Request(department_url, headers=headers)
    page_info = request.urlopen(page).read()
    soup = BeautifulSoup(page_info, 'html.parser')
    page_number = soup.find('a','p_text').get_text()[1:-1].strip()
    new_url = department_url[:-4]+'_' + page_number + '.htm'
    print(new_url)

def get_doctor_url(test_url):
    total_name_url = []
    page = request.Request(test_url, headers=headers)
    page_info = request.urlopen(page).read()
    soup = BeautifulSoup(page_info, 'html.parser')
    doctor_url = soup.find_all('a',href=re.compile('http://www.haodf.com/doctor\/((?!jingyan).)*htm'))
    for i in doctor_url:
        name_url = {'name':None, 'url':None}
        name_url['name'] = i.get_text()
        name_url['url'] = i.get('href')
        total_name_url.append(name_url)
    # return total_name_url
    for i in total_name_url:
        print(i)

def url_to_comment():
    test_url = 'http://www.haodf.com/doctor/DE4rO-XCoLUnz3tSkhlkqINLVW.htm'
    page = request.Request(test_url, headers=headers)
    page_info = request.urlopen(page).read()
    soup = BeautifulSoup(page_info, 'html.parser')
    text_info = soup.find_all('table','doctorjy')
    print(len(text_info))
    # for i in text_info:
    #     print(i)









if __name__ == '__main__':
    # info = getDepartmentUrl()
    # print(info[0])
    # url_transfer(info[0]['url'])
    #test_url = 'http://haoping.haodf.com/keshi/1010000/daifu_all_1.htm'
    #get_doctor_url(test_url)
    url_to_comment()