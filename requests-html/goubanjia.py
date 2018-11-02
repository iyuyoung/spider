from requests_html import HTMLSession
import re

session = HTMLSession()

# 使用requests-html 爬取IP代理
def parse():
    r = session.get('http://www.goubanjia.com')
    r.html.render()

    reg = re.compile('<p.*?/p*>|<.*?>', re.S)
    for x in r.html.find('.ip'):
        data = re.sub(reg, '', str(x.html))
        yield data


def main():
    for x in parse():
        # 存储代理地址 
        print(x)


if __name__ == '__main__':
    main()
