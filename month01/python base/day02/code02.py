"""
    算术运算符
"""
num01 = 5
num02 = 2
print(num01 % num02)
print(num01 % num02 != 0)

#练习1：在控制台中获取一个商品的单价 10
#       再获取一个商品的数量 3
#       再获取一个金额 50
#       计算：应该找回多少钱 20
#14：29

# price = float(input("Please input the price:"))
# count = int(input("Please input count:"))
# total_money = float(input("Please input total money:"))
# change = total_money - count * price
# print("The change is %s%d" % (change, 3))

#练习2：在控制台中获取小时/分钟/秒，计算总秒数。
# hours = int(input("Please input hours:"))
# minutes = int(input("Please input minutes:"))
# seconds = int(input("Please input seconds:"))
# minutes += hours * 60
# seconds += minutes * 60
# print("Total seconds is:" + str(seconds))

#练习3：古代的称一斤16两
#   在控制台中获取两，换算出是几斤几两
liang = int(input("请输入总两数："))
jin = liang // 16
liang = liang % 16
print("总共为" + str(jin) + "斤" + str(liang) + "两")