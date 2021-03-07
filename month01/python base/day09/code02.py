"""
    类成员
"""

class ICBC:
    """
    工商银行
    """
    money = 9999999

    @classmethod
    def get_total_moneys(cls):
        print(cls.money)

    def __init__(self, name, money):
        # 实例变量
        self.name = name
        self.money = money
        # 从总行中扣除目前支行现金
        ICBC.money -= money


i01 = ICBC("广渠门支行", 10000)
print(ICBC.money)
i02 = ICBC("磁器口支行", 10000)
print(ICBC.money)
ICBC.get_total_moneys()