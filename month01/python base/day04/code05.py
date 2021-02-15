"""
    字符串与列表
"""
# 根据某些逻辑，拼接字符串
result01 = []
for item in range(10):
    result01.append(str(item))

print("".join(result01))

str01 = "a-b-c-d-e-f-g"
list02 = str01.split("-")
print(list02)
