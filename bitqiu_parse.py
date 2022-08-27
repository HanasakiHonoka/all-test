import sqlite3

import requests,json

con = ""

def req(page):

    cookies = {
        'cloud_web_sid': 'b00efa74a291482194cf2113bec2c699',
        'cloud_web_uid': '110661697',
        'cloud_web_in': 'b49a1f8a11bb464f807bc3054f34219c',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'cloud_web_sid=b00efa74a291482194cf2113bec2c699; cloud_web_uid=110661697; cloud_web_in=b49a1f8a11bb464f807bc3054f34219c',
        'Origin': 'https://pan.bitqiu.com',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'User-Platform': 'ca4a9da1c26e535cb364551cb8e88069',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {'parentId': 'a3fcd57e985e4e718688e0ccc01b22aa', 'limit': '24', 'orderType': 'updateTime', 'desc': '1',
            'model': '1', 'userId': '110661697', 'name': 'undefined', 'currentPage': page,
            'org_channel': 'default|default|default'}

    response = requests.post('https://pan.bitqiu.com/apiToken/cfi/fs/resources/pages', cookies=cookies, headers=headers, data=data)

    res = json.loads(response.text)

    return res

def save_to_db(resource_id, name, create_time):
    cur = con.cursor()

    if len(cur.execute("select * from t_btq where resource_id = '%s'" % resource_id).fetchall()) > 0:
        print(name + " already exists")
        return

    sql = "insert into t_btq (resource_id, name, create_time) VALUES ('%s', \"%s\", '%s')" % (resource_id, name, create_time)
    try:
        cur.execute(sql)
        con.commit()
    except Exception:
        print(sql)
        print(Exception)


def update():
    curr_page = 1
    total_page = 1
    limit_page = 1
    while curr_page <= total_page and curr_page <= limit_page:
        res = req(curr_page)
        if res['code'] != '10200':
            print(res['code'])
            break
        total_page = res['data']['totalPageCount']
        data_list = res['data']['data']
        for item in data_list:
            resource_id = item['resourceId']
            name = item['name']
            create_time = item['createTime']
            save_to_db(resource_id, name, create_time)
        curr_page = curr_page + 1
    pass



if __name__ == '__main__':
    con = sqlite3.connect('./db/sql_lite.db')
    update()
    # print("`%s`" % "[MizudeppO] K_zuna AI's Virtual Sexgiving!.7z")
    con.close()
