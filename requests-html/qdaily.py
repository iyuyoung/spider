from requests_html import HTMLSession

session = HTMLSession()

# 使用requests-html 演示爬取 好奇心日报
def parse():
    r = session.get('http://www.qdaily.com/')
    r.html.render()
    # 获取首页新闻标签、图片、标题、发布时间
    for x in r.html.find('.packery-item'):
        yield {
            'tag': x.find('.category')[0].text,
            'image': x.find('.lazyload')[0].attrs['data-src'],
            'title': x.find('.smart-dotdotdot')[0].text if x.find('.smart-dotdotdot') else x.find('.smart-lines')[0].text,
            'addtime': x.find('.smart-date')[0].attrs['data-origindate'][:-6]
        }


def main():
    for x in parse():
        # 存储数据 
        print(x)


if __name__ == '__main__':
    main()
