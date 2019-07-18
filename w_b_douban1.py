#coding=gbk
import requests
from bs4 import BeautifulSoup

'''
    ���е�һ��ʵս�������ϰ�������ȡ���Ƕ�������
    ��Ҫ�������������ߵ���Ϣ�����֣����
'''
resp = requests.get('http://book.douban.com/top250?start=0')
#ץȡ����ǰ250���鼮

print(resp.text)#��ȡԴ��html

soup = BeautifulSoup(resp.text, 'lxml')#����html

#��ȡ���ߵ���Ϣ
allp = soup.find_all('p' ,class_='pl')
# ~ for p in allp:
    # ~ arthur = p.get_text()
    # ~ arthurs.append(arthur)
arthurs = [p.get_text() for p in allp]#��д��

#��ȡ����
alldiv = soup.find_all('div', class_='pl2')
booknames = [div.find('a')['title'] for div in alldiv]
#����ȡ����title�����������ݣ�������['title']������.get_text().

#��ȡ����
starspan = soup.find_all('span', class_='rating_nums')
scores = [s.get_text() for s in starspan]

#��ȡ���
sumspan = soup.find_all('span', class_='inq')
sums = [s.get_text() for s in sumspan]

#����ҳ��
url = 'http://book.douban.com/top250?start='
urls = [url + str(i) for i in range(0,226,25)]
for i in urls:
    resp = requests.get(i)
    
#��������ͷ
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

#�������
filename = '����TOP250�鼮.txt'
for bookname, arthur, score, sum_ in zip(booknames,arthurs,scores,sums):
    first_ = '������ ' + bookname + '\n'
    second_ = '���ߣ� ' + arthur + '\n'
    third_ = '���֣� ' + scores + '\n'
    forth_ = '��飺 ' + sum_ + '\n'
    data = first_ + second_ + third_ + forth_
    with open(filename, 'a', encoding='utf-8') as f_oj:
        f_oj.write(data + '*********************' + '\n')

