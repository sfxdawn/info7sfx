from flask import session
from . import index_blue


@index_blue.route('/')
def hello():
	session['name']='2018'
	return 'hello world2018'





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
#





































