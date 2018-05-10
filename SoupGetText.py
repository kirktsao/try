import re
import requests
import xlrd
import lxml
from bs4 import BeautifulSoup as bs
cas =7647-14-5
url='http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)
r = requests.get(url, timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
soup = bs(r.content,'lxml')
print(soup.text)