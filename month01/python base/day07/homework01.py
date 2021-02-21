# 1. 自定义列表排序函数
#    温馨提示：返回值需要吗？
def sort_list(list01):
    for i in range(len(list01)-1):
        for j in range(i,len(list01)):
            if list01[i] > list01[j]:
                list01[i], list01[j] = list01[j], list01[i]

list02 = [3,1,8,2,4,5]
sort_list(list02)
print(list02)

# 3. 英文单词反转，例如: how are you -> you are how
while True:
    str_input = input("请输入英文句子:")
    if str_input == "q":
        break
    list01 = str_input.split()
    list02 = list01[::-1]
    print(" ".join(list02))