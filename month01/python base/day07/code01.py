"""
    代码重构
"""
dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
shopping_list = list()


def show_product(product_info):
    print("1键购买，2键结算")
    for k, v in product_info.items():
        print("编号：%d 名称：%-5s  价格：%-6d" % (k, v["name"], v["price"]))


def add_shopping_list(id, count):
    if id not in dict_commodity_info:
        print("商品不存在！")
    else:
        shopping_list.append((id, count))


def compute_price():
    total_price = 0
    for item in shopping_list:
        print("商品编号%d：，数量%d" % (item[0], item[1]))
        total_price += dict_commodity_info[item[0]]["price"] * item[1]
    print("总价格是：%d" % total_price)
    return total_price


while True:
    show_product(dict_commodity_info)
    opcode = int(input("你输入你的操作："))
    if opcode == 1:
        while True:
            id = int(input("请输入商品编码："))
            if id in dict_commodity_info:
                break
            else:
                print("该商品不存在！")
        while True:
            count = int(input("请输入商品数量："))
            if count > 0:
                break
            else:
                print("商品数量不能小于0！")
        add_shopping_list(id, count)
    elif opcode == 2:
        total_price = compute_price()
        while True:
            input_money = int(input("请输入你的总金额："))
            if input_money < total_price:
                print("金额不足！")
            else:
                print("购买成功！找零：%d元" % (input_money - total_price))
                break
