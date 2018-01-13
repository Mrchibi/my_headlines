
# -*- coding:UTF-8 -*-
from __future__ import  unicode_literals
import feedparser
from flask import  Flask,render_template,request

app = Flask(__name__)#创建程序实例，该实例为flask类的对象，
#wsgi协议把接收到的请求转交给这个对象处理
RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml",
            
            }#RSS字典




@app.route('/')#执行的视图函数


def get_news(publication="zhihu"):
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEED:
        publication = "songshuhui"
    else:
        publication =query.lower()
    
    feed = feedparser.parse(RSS_FEED[publication])#parse函数解析rss
    
    return render_template('home.html',articles=feed['entries'])#feed['entries']表示一组文章的条目
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)#执行该脚本时才启动程序