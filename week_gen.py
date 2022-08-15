
# encoding: utf-8

import csv

with open("D:\DataScience\\box22.csv", encoding='utf-8') as f:
    rf = csv.reader(f)
    movie = ''
    cnt = 0
    for row in rf:
        if movie != row[2]:
            movie = row[2]
            cnt = 0
        else:
            cnt = cnt + 1
        ss = ','.join([row[0],row[1],row[2],row[3],row[4],row[5], str(cnt), str(int(cnt/7))])
        print(ss)