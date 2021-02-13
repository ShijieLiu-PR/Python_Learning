""""""
"""
    循环语句
        --while
"""
while True:
    str_usd = input("Pleaes input dollar:")
    float_usd = float(str_usd)
    rmb = float_usd * 6.708
    print(rmb)
    if(input("Press e to exit:")) == "e":
        break
# 练习3：在控制台中分别输入两个整数，一个作为开始值，一个作为结束值，请输入中间数字。