# 自动化爬取腾讯漫画《海贼王》
import urllib.request
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import string
import os

data = urllib.request.urlopen("http://ac.qq.com/Comic/comicInfo/id/505430").read()

soup = BeautifulSoup(data,'html5lib')

itemlist = soup.find_all(href=re.compile("/ComicView/index/id/505430/cid/"))
del itemlist[0]
del itemlist[0]
del itemlist[0]
ilist = [];
itemlist.reverse()
for iteml in itemlist:
	
	print(iteml.attrs['title'])
	url = "http://ac.qq.com"+iteml.attrs['href']

	'''ti = iteml.attrs['title']
	ilist.append(ti)

istr = '\n'.join(ilist)
with open('d:/test/222.txt','w',encoding='utf-8') as file:
	file.write(istr)
	file.close()'''
		


	driver=webdriver.Firefox()               
	driver.get(url)   

	driver.execute_script("window.scrollTo(0,2000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(2000,4000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(4000,6000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(6000,9000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(9000,12000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(12000,15000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(15000,18000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(18000,20000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(20000,23000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(23000,26000);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(26000,30000);")
	time.sleep(3)
	


	html=driver.page_source
	soup1=BeautifulSoup(html,'html5lib')

	items=soup1.find_all(src=re.compile("store_file_download"))

	mkpath = 'D:\\test\\'+iteml.attrs['title'][8:]+'\\'
	os.mkdir(mkpath)
	n = 1
	for item in items:
				print(item['src'])
				urllib.request.urlretrieve(url=item['src'],filename='D:\\test\\'+iteml.attrs['title'][8:]+'\\'+str(n)+'.jpg')
				n = n + 1
	driver.quit()
	       
