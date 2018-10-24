from flask import Blueprint

index_blue=Blueprint("index_blue",__name__)

from . import views




# from flask import Blueprint
#
# # 编写一个 武术-蓝图 功能 模块
# # 后面括号里面的
# # 第一个参数：是这个 模块的名字 我说我要写一个 武术模块，那么这个模块 就叫武术 或者 功夫
# # 第二个参数：当前 武术-蓝图 所在的 位置， 包的名称。
# # 第一个 index_blue 是 这个芯片外面贴的标签 上的名称，不然很多 功能模块放在一起无法区分，弄混了。
#
# index_blue=Blueprint("index_blue",__name__)
#
# # 为什么要在这里导入 views 啊？
# # 本来 views.py文件 里面写的东西 就是这里面的，
# # 你看我编写一个 功夫程序，现在，只写了个标题  然后里面的内容(各种武术招式) 被分割到其他地方去了(具体放在 views文件里面去了)
# # 这样标题下面就不完整了呀，再把 views 里面的 武术招式 内容 拿过来。
#
# from . import views
#



































