#coding=gbk
import requests
from bs4 import BeautifulSoup
import random
import time

'''
    ���е�һ��ʵս�������ϰ�������ȡ���Ƕ�������
    ��Ҫ�������������ߵ���Ϣ�����֣����
'''

def all_urls():
    '''����ҳ��'''
    url = 'http://book.douban.com/top250?start='
    urls = [url + str(i) for i in range(0,226,25)]
    return urls

def read_data(soup):
    '''ץȡ���ݲ�����'''
    #��ȡ���ߵ���Ϣ
    allp = soup.find_all('p' ,class_='pl')
    arthurs = [p.get_text() for p in allp]
    
    time.sleep(2)
    
    #��ȡ����
    alldiv = soup.find_all('div', class_='pl2')
    booknames = [div.find('a')['title'] for div in alldiv]
    
    time.sleep(2)
    
    #��ȡ����
    starspan = soup.find_all('span', class_='rating_nums')
    scores = [s.get_text() for s in starspan]
    
    time.sleep(2)
    
    #��ȡ���
    sumspan = soup.find_all('span', class_='inq')
    sums = [s.get_text() for s in sumspan]
    
    time.sleep(2)
    
    #�������
    filename = '����TOP250�鼮.txt'
    for bookname, arthur, score, sum_ in zip(booknames,arthurs,scores,sums):
        first_ = '������ ' + bookname + '\n'
        second_ = '���ߣ� ' + arthur + '\n'
        third_ = '���֣� ' + str(score) + '\n'
        forth_ = '��飺 ' + sum_ + '\n'
        data = first_ + second_ + third_ + forth_
        with open(filename, 'a', encoding='utf-8') as f_oj:
            f_oj.write(data + '*********************' + '\n')

def main():
    '''������'''
    urls = all_urls()
    i = 1#������
    for urls_page in urls:#�ֱ�ץȡ10ҳ
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}#��������ͷ
        resp = requests.get(urls_page, headers=headers)#ץȡ����ǰ250���鼮
        soup = BeautifulSoup(resp.text, 'lxml')#����html
        read_data(soup)#ץȡ����
        print('��{}ҳ����ɹ�,��10ҳ��'.format(i))
        i += 1
        time.sleep(2)
        
    
if __name__ == '__main__':
    main()
