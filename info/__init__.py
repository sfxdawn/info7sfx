from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import config


from logging.handlers import RotatingFileHandler
import logging

logging.basicConfig(level=logging.DEBUG)

file_log_handler=RotatingFileHandler("logs/log",maxBytes=1024*1024*100,backupCount=10)

formatter =logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s ')

file_log_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_log_handler)






db=SQLAlchemy ()

def create_app(config_name):

	app=Flask (__name__)

	app.config.from_object (config[config_name])

	db.init_app(app)

	Session (app)
	from info.modules.index import index_blue
	app.register_blueprint(index_blue)
	return app





# ----------------------设置日志-----------------------------------------------------------


# from logging.handlers import RotatingFileHandler     #这个是标准模块，可以自动导入的。
# import logging


# logging.basicConfig(level=logging.DEBUG)       #调试 debug 级
#
# file_log_handler=RotatingFileHandler("logs/log",maxBytes=1024*1024*100,backupCount=10)
#
# # file_log_handler ⭐️创建日志记录本，      指明日志保存的路径，每个日志文件的最大 ，保存文件个数上限
# # Rotating 旋转，123456789 10 塞满了就把1删除了，把1位置改成11，
#
# formatter =logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s ')
#
# # ⭐️设置写日记的格式      日记怎么写才规范       日志等级      日志信息的文件名   行数        日志信息
#
# file_log_handler.setFormatter(formatter)
#
# # ⭐️把写日记的格式应用在 日记记录本上， 这样日记就不会乱写了，写日记也是有规范的。
#
# logging.getLogger().addHandler(file_log_handler)
#
# # 把 日志记录本  发给 公司的每个人， ⭐️公司每个人都要写日记

# ------------------------------------------------------------------------------------------------



# db=SQLAlchemy ()                      # 先做一个机器人空骨架
#
# # 工厂函数：让 app 通过函数进行调用，可以根据传入的参数的不同，动态的生产不同模式下的 app
# def create_app(config_name):
#
# 	app=Flask (__name__)
#
# 	app.config.from_object (config[config_name])
#
# 	db.init_app(app)                  # 插入人工智能芯片 app 让机器人骨架 和芯片结合，并且初始化 芯片app.
#
# 	Session (app)                     # 设置 session 保存位置
#
# 	# 花钱购买--也就是所谓的⭐️注册--功夫模块(index_blue) 你注册了人家才让你使用啊， 注册之前 先导入。。。。
# 	# 不然，人家辛辛苦苦写出来的 功夫功能模块 ，让你免费使用啊，中国人爱搞盗版。。。
# 	from info.modules.index import index_blue
# 	app.register_blueprint(index_blue)
#
# 	return app








