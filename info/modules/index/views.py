from flask import session, render_template, current_app
from . import index_blue


@index_blue.route('/')
def hello():
	session['name']='2018'
	return render_template('news/index.html')


@index_blue.route('/favicon.ico')
def favicon():
	return current_app.send_static_file('news/favicon.ico')













# from flask import session
#
# # 为什么要导入 index_blue 啊，
# # 哎，这个 index_blue 是 这个模块外面贴的的标签，没有标签，这个内容就找不到了。
# # （这个模块是武术模块的招式内容不包括标题）
# # Map([<Rule '/' (GET, OPTIONS, HEAD) -> index_blue.hello>，
# # index_blue.hello   前面的 index_blue  是在说 这个谁家的 功能模块 哦，这是 功夫功能模块下的招式 hello ，招手过来~，挑衅招，
#
# from . import index_blue
#
#
# @index_blue.route('/')
# def hello():
# 	session['name']='2018'
# 	return 'hello world2018'
#   return render_template('news/index.html')
# 应用模板了 模板里面的 news 文件夹，下面的 index.html
# 默认访问同级目录下的 看源码，
# 后面的代码实现 log 小图标加载

# @index_blue.route ('/favicon.ico')
# def favicon():
# 	# 项目 title 标签中的 logo 图标
# 	# 浏览器会默认访问项目根目录下的 favicon.ico 文件
# 静态路径 flask 会默认创建，拼接 favicon 文件所在的路径即可
# http://127.0.0.1:5000/static/news/favicon.ico
# send_static_file 函数的作用是把 static 文件夹下的文件发送给浏览器
# 第一次实现可能浏览器加载不到 favicon 文件，
# 1.需要先清理浏览器缓存，2，浏览器彻底退出重新启动。
#  	return current_app.send_static_file ('news/favicon.ico')
# 什么叫 当前 app  current_app  功夫大师回家去取头衔了。 app=Flask(__name__) 这就是家，
# 这次回去是有目的的，在加载功夫模块之前， 就去访问了 static 文件夹 然后用一个方法 直接把 头衔 发送给了浏览器，
# 这个方法就是 send_static_file()   如果他不回家，他就无法发送 头衔证明文件 给 武术协会，获得认证。




































