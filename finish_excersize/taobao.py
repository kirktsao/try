import requests
import re
#from bs4 import BeautifulSoup
#url = 'http://www.bestbiotech.com.cn/shop/product/search?search=type&keyword='+str(cas)+'&pagesize=30'
#cas = '7647-14-5'

#获得网页文本
def getTextHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

#解析网页
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        return ''

#输出价格清单
def printGoodlist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品信息"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

#主函数
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s='+ str(44*i)
            html = getTextHtml(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodlist(infoList)

main()
