"""
    包
        python程序结构
"""

# 方式1：import bao.模块
import package01.module01
# 使用：包.模块.成员

# 方式2：from 包 import 模块
from package01 import module01
# module01.fun01()

# 方式3：from 包 import *
from package01 import *
# module01.fun01()

import sys
from package01.module01 import *
fun01()

print(sys.path)