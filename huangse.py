import requests
from lxml import etree

def work1():

    start = 7788683
    s1 = set()

    for i in range(1):
        url = 'http://www.bamxs.com/view.asp?id=%d' % (i + start)
        data = requests.get(url)
        # data.encoding = 'utf-8'
        s = etree.HTML(data.text)
        # res = s.xpath('//td/img/@src')
        res = s.xpath("//td[@class='content']")
        for url in res:
            print(url)
            # s1.add(url)

    print(len(s1))
    for i in s1:
        print(i)
    pass

def work2():
    htmldemo = '''
    <meta charset="UTF-8"> <!-- for HTML5 -->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <html><head><title>yoyo ketang</title></head>
    <body>
    <b><!--Hey, this in comment!--></b>
    <p class="title"><b>yoyoketang</b></p>
    <p class="yoyo">这里是我的微信公众号：yoyoketang
    <a href="http://www.cnblogs.com/yoyoketang/tag/fiddler/" class="sister" id="link1">fiddler教程</a>,
    <a href="http://www.cnblogs.com/yoyoketang/tag/python/" class="sister" id="link2">python笔记</a>,
    <a href="http://www.cnblogs.com/yoyoketang/tag/selenium/" class="sister" id="link3">selenium文档</a>;
    快来关注吧！</p>
    <p class="story">...</p>
    '''

    # etree.HTML解析html内容
    demo = etree.HTML(htmldemo)
    # 打印解析内容str
    t = etree.tostring(demo, encoding="utf-8", pretty_print=True)

    print(t.decode("utf-8"))
    pass

if __name__ == '__main__':
    work1()
    pass