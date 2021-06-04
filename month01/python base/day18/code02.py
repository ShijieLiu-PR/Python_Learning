"""
    闭包
"""


def fun01():
    print("fun01 is running")
    a = 1

    def fun02():
        print("fun02 is running")
        print("外部变量是：", a)

    return fun02


result = fun01()
result()

# 案例：
#


def get_gift_money(money):
    print("get money %d" % money)

    def child_buy(target, price):
        nonlocal money
        if money >= price:
            money -= price
            print("child spend %d dollar to buy %s." % (price, target))
        else:
            print("money is not enough.")
    return child_buy

result = get_gift_money(10000)
result("book", 200)
result("book", 400)


