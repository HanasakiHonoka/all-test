import sqlite3

import requests
from lxml import etree
import re
import os

def test():
    url = 'https://sukebei.nyaa.si/?f=0&c=1_1&q='

    text = requests.get(url).text

    # print(text)

    html = etree.HTML(text)

    res = html.xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/a[last()]/text()")
    print(res)
    pass

if __name__ == '__main__':
    test()