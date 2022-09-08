import sqlite3

import requests
from lxml import etree
import re
import os

con = ""
def parse_rj_title_cv(rj_num):
    url = 'https://www.dlsite.com/maniax/work/=/product_id/RJ%s.html' % (rj_num)

    text = requests.get(url).text

    # print(text)

    html = etree.HTML(text)

    cv_name = html.xpath('//*[@id="work_outline"]//tr[3]/td/a/text()')
    title = html.xpath('//*[@id="work_name"]/text()')
    # items = html.xpath('//a/text()')
    return cv_name, title

def parse_rj_title_cv_test(rj_num):
    if rj_num == "213123":
        return ["cv1"], "name1"
    elif rj_num == "1234214":
        return ["cv2", "cv21"], "name2"
    elif rj_num == "21312312":
        return ["cv3", "cv4"], "name3"


# print(re.findall("\d{2,}", "RJ305514-バブバブの森_彼女のお姉ちゃんは赤ちゃん言葉で浮気誘惑mp3"))
# def db_test():
#     con = sqlite3.connect('./db/sql_lite.db')
#
#     cur = con.cursor()
#
#     res = cur.execute("select * from t_voice").fetchall()
#
#     print(res)
#
#     con.close()

def get_rj_dir_name(rj_num):
    cur = con.cursor()
    res = cur.execute("select * from t_voice where rj_num = '%s'" % rj_num).fetchall()
    cv = None
    title = None
    if len(res) < 1:
        cv, title = parse_rj_title_cv(rj_num)
        cv = '、'.join(cv)
        title = ''.join(title)

        sql = "insert into t_voice(title, rj_num, cv) Values ('%s', '%s', '%s')" % (title, rj_num, cv)
        cur.execute(sql)
        con.commit()
    else:
        cv = res[0][3]
        title = res[0][1]
    if cv is not None and title is not None:
        title = title.replace(":", "")
        return '''RJ%s-%s-%s''' % (rj_num, title, cv)
    else:
        return "error"
    pass

def work():
    # top_dir = "/Users/xuzixiang/linshi/voice"
    top_dir = "E:\\Voice"
    for dir in os.listdir(top_dir):
        if dir == ".DS_Store":
            continue
        if dir.find("-") > 0:
            continue
        rj_num = re.findall("\d{2,}", dir)
        if len(rj_num) < 1:
            continue
        new_name = get_rj_dir_name(rj_num[0])
        if new_name == "error":
            continue
        os.rename(top_dir+'\\'+dir, top_dir+'\\'+new_name)
        # break


if __name__ == '__main__':
    # parse_rj_title_cv("394238")
    con = sqlite3.connect('../db/sql_lite.db')
    work()
    # print(parse_rj_title_cv('305514'))
    con.close()