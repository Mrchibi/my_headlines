
# -*- coding:UTF-8 -*-
from __future__ import  unicode_literals
import feedparser
from flask import  Flask

app = Flask(__name__)#创建程序实例，该实例为flask类的对象，
#wsgi协议把接收到的请求转交给这个对象处理
RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml"}#RSS字典




@app.route('/')
@app.route('/zhihu')
def zhihu():
    return get_news('zhihu')

@app.route('/netease')
def netease():
    return get_news('netease')

def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])#parse函数解析rss
    first_content = feed['entries'][0]
    html_format="""
    <html> <body>
        <h1> Zhihu Headlines </h1>
        <b> {0} </b> <br/>
        <i> {1} </i> <br/>
        <p> {2} </p> <br/>
    <body> </html>"""
    return html_format.format(first_content.get('title'),first_content.get('published'),first_content.get('summary'))
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)#执行该脚本时才启动程序