# 练习3：在控制台中显示120秒倒计时，02:00  01:59 ... 00:00
# seconds = int(input("Please input seconds:"))
# while True:
#     min = seconds // 60
#     sec = seconds % 60
#     print("%02d:%02d" % (min, sec))
#     seconds -= 1
#     if seconds < 0:
#         break

for item in range(120,-1,-1):
    min = item // 60
    sec = item % 60
    print("%02d:%02d" %(min, sec))
