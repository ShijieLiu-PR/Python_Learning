# 练习2：经理[曹操，刘备，孙权]  技术员[曹操，刘备，张飞，关羽],计算：
# 1.既是经理也是技术员的有谁？
# 2.是经理但不是技术员的有谁？
# 3.是技术员，但不是经理的有谁？
# 4.张飞是经理吗？
# 5.身兼一职的都有谁？
# 6.经理和技术员总共有多少人？
manager = frozenset(["曹操","刘备","孙权"])
technician = frozenset(["曹操","刘备","张飞","关羽"])
# 1.既是经理也是技术员的有谁？
s01 = manager & technician
print(s01)
# 2.是经理但不是技术员的有谁？
s02 = manager - technician
print(s02)
# 3.是技术员，但不是经理的有谁？
s03 = technician - manager
print(s03)
# 4.张飞是经理吗？
print("张飞" in manager)
# 5.身兼一职的都有谁？
s04 = manager ^ technician
print(s04)
# 6.经理和技术员总共有多少人？
s05 = manager | technician
print(s05)
print(len(s05))