#coding=gbk
import requests
from bs4 import BeautifulSoup
import random
import time

'''
    进行第一次实战爬虫的练习，这次爬取的是豆瓣网。
    需要的是书名，作者等信息，评分，简介
'''

def all_urls():
    '''更换页数'''
    url = 'http://book.douban.com/top250?start='
    urls = [url + str(i) for i in range(0,226,25)]
    return urls

def read_data(soup):
    '''抓取数据并保存'''
    #爬取作者等信息
    allp = soup.find_all('p' ,class_='pl')
    arthurs = [p.get_text() for p in allp]
    
    time.sleep(2)
    
    #爬取书名
    alldiv = soup.find_all('div', class_='pl2')
    booknames = [div.find('a')['title'] for div in alldiv]
    
    time.sleep(2)
    
    #爬取评分
    starspan = soup.find_all('span', class_='rating_nums')
    scores = [s.get_text() for s in starspan]
    
    time.sleep(2)
    
    #爬取简介
    sumspan = soup.find_all('span', class_='inq')
    sums = [s.get_text() for s in sumspan]
    
    time.sleep(2)
    
    #打包数据
    filename = '豆瓣TOP250书籍.txt'
    for bookname, arthur, score, sum_ in zip(booknames,arthurs,scores,sums):
        first_ = '书名： ' + bookname + '\n'
        second_ = '作者： ' + arthur + '\n'
        third_ = '评分： ' + str(score) + '\n'
        forth_ = '简介： ' + sum_ + '\n'
        data = first_ + second_ + third_ + forth_
        with open(filename, 'a', encoding='utf-8') as f_oj:
            f_oj.write(data + '*********************' + '\n')

def main():
    '''主函数'''
    urls = all_urls()
    i = 1#计数器
    for urls_page in urls:#分别抓取10页
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}#设置请求头
        resp = requests.get(urls_page, headers=headers)#抓取豆瓣前250的书籍
        soup = BeautifulSoup(resp.text, 'lxml')#解析html
        read_data(soup)#抓取数据
        print('第{}页保存成功,共10页。'.format(i))
        i += 1
        time.sleep(2)
        
    
if __name__ == '__main__':
    main()
