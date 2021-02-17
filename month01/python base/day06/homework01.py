"""
    day06作业：
    1. 参照下列代码，定义判断是否是奇数的方法。
    2. 参照下列代码，定义根据月份返回天数的方法。要求：考虑2月，如果是闰年返回29天，否则返回28天。
    3. 参照如下代码，定义获取最小值的方法
    4. 定义函数，判断字符串中存在的中文字符数。中文编码范围：0x4E00 --> 0x9FA5
    5. 定义函数，计算指定范围内的素数。例如1-100之间。
"""
# 1. 参照下列代码，定义判断是否是奇数的方法。
def is_odd(number):
    if number %2 != 0:
        return True
    else:
        return False
# 2. 参照下列代码，定义根据月份返回天数的方法。要求：考虑2月，如果是闰年返回29天，否则返回28天。
def days_of_month(month,year):
    if month == 2:
        leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        return 29 if leap else 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [2,4,6,9,11]:
        return 30
    else:
        return 0

print(days_of_month(4,2009))

# 3. 参照如下代码，定义获取最小值的方法
def find_min(list01):
    result = list01[0]
    for item in list01:
        if result > item:
            result, item = item, result
    return result

print(find_min([4,1,7,2]))

# 4. 定义函数，判断字符串中存在的中文字符数。中文编码范围：0x4E00 --> 0x9FA5
def count_character(str_input):
    count = 0
    for item in str_input:
        if 0x4E00 <= ord(item) <= 0x9FA5:
            count += 1
    return count

print(count_character("abc 你bu是一个hao人"))

# 5. 定义函数，计算指定范围内的素数。例如1-100之间。
def find_prime(low,high):
    prime_list = list()
    for item in range(low,high+1):
        result = True
        for i in range(2,item,1):
            if item % i == 0:
                result = False
                break
        if result:
            prime_list.append(item)
    return prime_list

print(find_prime(10,2022))