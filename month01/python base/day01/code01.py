"""
    汇率转换器
    输入美元，显示人民币
"""


#1.获取数据
str_usd = input("请输入美元:")
float_usd = float(str_usd)

#2.逻辑处理
rmb = float_usd * 6.708

# 3.显示结果
print(rmb)

"""
    pycharm常用的快捷键
    1. 移动到本行的开头：home
    2. 移动到本行的末尾：end
    3. 复制一行代码：Ctrl+D
    4. 注释代码：Ctrl+/
    5. 选择列并多列输入：鼠标左键+Alt
    6. 移动行：shift+alt+上下箭头，或者用ctrl+shift+上下箭头
    7. 智能提示：ctrl+空格
"""
