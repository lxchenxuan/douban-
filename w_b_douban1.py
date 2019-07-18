#coding=gbk
import requests
from bs4 import BeautifulSoup

'''
    进行第一次实战爬虫的练习，这次爬取的是豆瓣网。
    需要的是书名，作者等信息，评分，简介
'''
resp = requests.get('http://book.douban.com/top250?start=0')
#抓取豆瓣前250的书籍

print(resp.text)#获取源码html

soup = BeautifulSoup(resp.text, 'lxml')#解析html

#爬取作者等信息
allp = soup.find_all('p' ,class_='pl')
# ~ for p in allp:
    # ~ arthur = p.get_text()
    # ~ arthurs.append(arthur)
arthurs = [p.get_text() for p in allp]#简写，

#爬取书名
alldiv = soup.find_all('div', class_='pl2')
booknames = [div.find('a')['title'] for div in alldiv]
#这里取的是title，而不是内容，所以用['title']而不用.get_text().

#爬取评分
starspan = soup.find_all('span', class_='rating_nums')
scores = [s.get_text() for s in starspan]

#爬取简介
sumspan = soup.find_all('span', class_='inq')
sums = [s.get_text() for s in sumspan]

#更换页数
url = 'http://book.douban.com/top250?start='
urls = [url + str(i) for i in range(0,226,25)]
for i in urls:
    resp = requests.get(i)
    
#设置请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

#打包数据
filename = '豆瓣TOP250书籍.txt'
for bookname, arthur, score, sum_ in zip(booknames,arthurs,scores,sums):
    first_ = '书名： ' + bookname + '\n'
    second_ = '作者： ' + arthur + '\n'
    third_ = '评分： ' + scores + '\n'
    forth_ = '简介： ' + sum_ + '\n'
    data = first_ + second_ + third_ + forth_
    with open(filename, 'a', encoding='utf-8') as f_oj:
        f_oj.write(data + '*********************' + '\n')

