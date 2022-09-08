
import requests
from lxml import etree

def test():
    url = 'https://tieba.baidu.com/p/2178895738'

    text = requests.get(url).text

    # print(text)

    html = etree.HTML(text)

    # res = html.xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/a[last()]/text()")
    print(text)
    pass

if __name__ == '__main__':
    test()