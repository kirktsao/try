##Import Module
import re
import requests
import xlwt
import lxml
from bs4 import BeautifulSoup as bs

##Input CAS number by user
#cas = input('Please Input CAS Number:')

def getTextHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
        
def main():
#    yf = []
    try:
        cas =7647-14-5
        url='http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)
        html = getTextHtml(url)
        reg = re.compile(r'class='product_div '',re.S)
        items = re.findall(reg,html)
        print(items)
    except:
        return ''

main()
