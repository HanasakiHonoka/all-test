import re
import sqlite3

import requests, json

from my_models import TBtqResource

con = ""

def build_from_json(data):
    # data = json.loads(json_str)
    tbr = TBtqResource(
        resourceId=data['resourceId'],
        resourceUid=data['resourceUid'],
        resourceType=data['resourceType'],
        parentId=data['parentId'],
        name=data['name'],
        extName=data['extName'],
        size=data['size'],
        createTime=data['createTime'],
        updateTime=data['updateTime'],
        sort=data['sort'],
        collect=data['collect'],
        hidden=data['hidden'],
        dirType=data['dirType'],
        dirLevel=data['dirLevel'],
        type=data['type'],
        fileMd5=data['fileMd5'],
        isView=data['isView'],
        src=data['src'],
        viewUrl=data['viewUrl'],
    )
    return tbr

def req(page, parent_id):
    cookies = {
        'cloud_web_sid': '18699287d9d548b6bf7f48592a7fd51e',
        'cloud_web_uid': '110661697',
        'cloud_web_in': 'd3864dfda12d421ab96b10bc3239ab7c',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # cloud_web_sid=18699287d9d548b6bf7f48592a7fd51e; cloud_web_uid=110661697; cloud_web_in=d3864dfda12d421ab96b10bc3239ab7c
        # 'Cookie': 'cloud_web_sid=b00efa74a291482194cf2113bec2c699; cloud_web_uid=110661697; cloud_web_in=b49a1f8a11bb464f807bc3054f34219c',
        'Origin': 'https://pan.bitqiu.com',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'User-Platform': 'ca4a9da1c26e535cb364551cb8e88069',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {'parentId': parent_id, 'limit': '24', 'orderType': 'updateTime', 'desc': '1',
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

def get_bangumi():
    cur = con.cursor()
    res = cur.execute("select name from t_btq").fetchall()
    for name in res:
        if len(re.findall("[a-zA-Z]+-\d+", name[0])) > 0:
            if name[0].find("HEVC-10bit") > 0:
                continue
            print(name[0])
        # print(name[0], re.findall("[a-zA-Z]+-\d+", name[0]))


def get_limit_by_parent(parent):
    return 2


def parse_dir_data(parent, page, has_next):
    if has_next and page <= get_limit_by_parent(parent):
        res_json = req(page, parent)
        if res_json['code'] != '10200':
            print(res_json['code'])
            return
        data_list = res_json['data']['data']
        has_next = res_json['data']['hasNext']
        for item in data_list:
            tbr = build_from_json(item)
            tbr.save()
            if item['resourceType'] == 1:
                parse_dir_data(item['resourceId'], 1, True)
        if has_next:
            parse_dir_data(parent, page+1, has_next)
    pass


def test():
    # res = req(1, "a3fcd57e985e4e718688e0ccc01b22aa")
    # if res['code'] != '10200':
    #     print(res['code'])
    #     return
    # data_list = res['data']['data']
    # for item in data_list:
    #     resourceId = item['resourceId']
    #     resourceType = item['resourceType']
    #     parentId = item['parentId']
    #     name = item['name']
    #
    #     print()
    tbr = TBtqResource()
    tbr_json = '''
    {
	"resourceId": "a3fcd57e985e4e718688e0ccc01b22aa",
	"resourceUid": "a3fcd57e985e4e718688e0ccc01b22aa",
	"resourceType": 1,
	"parentId": "f5ff0ea126c24b0ea20d7332bb88e9ca",
	"name": "云下载",
	"extName": null,
	"size": null,
	"createTime": "2019-09-19 14:54:32",
	"updateTime": "2022-09-03 01:56:21",
	"sort": "eyJpZCI6ImEzZmNkNTdlOTg1ZTRlNzE4Njg4ZTBjY2MwMWIyMmFhIiwidHlwZSI6MSwibmFtZSI6IuS6keS4i+i9vSIsIm5hbWVTb3J0IjoiOGM4YjhkIiwic2l6ZSI6bnVsbCwidGltZSI6MTY2MjE0MTM4MTAwMH0=",
	"collect": 0,
	"hidden": 0,
	"dirType": 1,
	"dirLevel": 1,
	"type": null,
	"fileMd5": null,
	"isView": 0,
	"src": null,
	"viewUrl": null
}
    '''
    json_obj = json.loads(tbr_json.strip())
    tbr = build_from_json(tbr_json)
    print(tbr)
    pass




if __name__ == '__main__':
    # con = sqlite3.connect('../db/sql_lite.db')


    # # update()
    # # get_bangumi()
    # res_json = req(1, "f5ff0ea126c24b0ea20d7332bb88e9ca")
    # rr = res_json['data']['hasNext']
    # print(rr)
    print(req(1, "a3fcd57e985e4e718688e0ccc01b22aa"))
    # parse_dir_data("a3fcd57e985e4e718688e0ccc01b22aa", 1, True)
    # # print("`%s`" % "[MizudeppO] K_zuna AI's Virtual Sexgiving!.7z")
    # con.close()
