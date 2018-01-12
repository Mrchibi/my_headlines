
# -*- coding:UTF-8 -*-
from flask import  Flask

app = Flask(__name__)#创建程序实例，该实例为flask类的对象，
#wsgi协议把接收到的请求转交给这个对象处理




@app.route('/')#声明路由
def get_news():
    return "no news is good news"#函数返回值为响应
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)#执行该脚本时才启动程序