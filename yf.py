##一方
#url='http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)+'&pagesize=30'
from urllib import request
from bs4 import BeautifulSoup as bs
import re
cas = str(71-43-2)
resp = request.urlopen('http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)+'&pagesize=30')
html_data = resp.read().decode('utf-8')
soup=bs(html_data,'lxml')
result_cas = soup.find_all('table',class_='tab_res')
result_cas_list = result_cas[0].find_all('a',text="True")
print(result_cas_list)
