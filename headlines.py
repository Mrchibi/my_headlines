
# -*- coding:UTF-8 -*-
from __future__ import  unicode_literals
import feedparser
from flask import  Flask,render_template

app = Flask(__name__)#创建程序实例，该实例为flask类的对象，
#wsgi协议把接收到的请求转交给这个对象处理
RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml",
            
            }#RSS字典




@app.route('/')#执行与/<publication>一样的视图函数
@app.route('/<publication>')#使用动态路由获取不同网站的headlines

def get_news(publication="zhihu"):
    feed = feedparser.parse(RSS_FEED[publication])#parse函数解析rss
    first_content = feed['entries'][0]
    
    
    return render_template('home.html',article=first_content)
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)#执行该脚本时才启动程序