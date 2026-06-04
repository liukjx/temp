"""
在python中，模块导入方式有两种
    ① import
        import 模块名称
    ② from 模块名 import 方法
        from 模块名称 import 函数名  代码只导入对应的函数 不全部导入（推荐）
    ③import 模块名称 as 定义别名
"""

from os import mkdir, rmdir
import random as rm