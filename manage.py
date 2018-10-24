from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db,models


app=create_app('development')
manager=Manager (app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
	print(app.url_map)
	manager.run ()




# from flask import session
#
# # 导入 flask_script
# from flask_script import Manager
#
# # 导入数据库迁移的扩展
# from flask_migrate import Migrate,MigrateCommand
# from info import create_app,db,models
#
#
# # 调用生成 app 的函数，传入不同的配置信息。
# app=create_app('development')
#
# # 把 app 交给职业经理人来管理
# manager=Manager (app)
#
# Migrate(app,db)    # 把 智能芯片 app 里面的意识 导入到 db 人工智能机器人 内存里面去。
#
# manager.add_command('db',MigrateCommand)       # 使用迁移框架
#
#
# if __name__ == '__main__':
# 	print(app.url_map)
# 	manager.run ()




