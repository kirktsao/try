import requests
from bs4 import BeautifulSoup as bs
cas = str(7647-14-5)
resp = requests.get('http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)+'&pagesize=30')
html_data = resp.read().decode('utf-8')
soup=bs(html_data,'html.parser')
result_cas = soup.find_all('table',class_='tab_res')
result_cas_list = result_cas[0].find_all('td',class_='product_div')
print(result_cas_list)
