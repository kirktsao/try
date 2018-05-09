##Import Module
import re
import requests
from bs4 import BeautifulSoup as bs

##Input CAS number by user
#cas = input('Please Input CAS Number:')
cas = str(7647-14-5)

url='http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)
def getTextHtml(url):
    try:
        soup = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

#解析网页
#def parsePage(ilt,html):
#    try:
#        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
#        pnm = re.findall(r'\"raw_title\"\:\".*?\"',html)
#        cnm =
#        sto = 
#        bra =
#        siz =
#        ano =
#        for i in range(len(plt)):
#            price = eval(plt[i].split(':')[1])
#            title = eval(tlt[i].split(':')[1])
#            ilt.append([price,title])
#    except:
#        return ''
def main():
#    yf = []
    try:
        html = getTextHtml(url)
        print(html)
    except:
        return ''

main()
