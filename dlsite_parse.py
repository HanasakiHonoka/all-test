import sqlite3

import requests
from lxml import etree
import re


def parse_rj_title_cv(rj_num):
    url = 'https://www.dlsite.com/maniax/work/=/product_id/RJ%s.html' % (rj_num)

    text = requests.get(url).text

    # print(text)

    html = etree.HTML(text)

    cv_name = html.xpath('//*[@id="work_outline"]//tr[3]/td/a/text()')
    title = html.xpath('//*[@id="work_name"]/text()')
    # items = html.xpath('//a/text()')
    print(cv_name, title)

# print(re.findall("\d{2,}", "RJ305514-バブバブの森_彼女のお姉ちゃんは赤ちゃん言葉で浮気誘惑mp3"))
def db_test():
    con = sqlite3.connect('mydatabase.db')

    cursorObj = con.cursor()

    con.close()


if __name__ == '__main__':
    # parse_rj_title_cv("394238")
    db_test()