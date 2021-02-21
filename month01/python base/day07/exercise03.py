# 练习3：定义函数，根据天/小时/分钟，计算总秒数。
def calculate_sec(day = 0, hour = 0, mins = 0):
    return ((day * 24 + hour) * 60 + mins) * 60


print(calculate_sec(1))