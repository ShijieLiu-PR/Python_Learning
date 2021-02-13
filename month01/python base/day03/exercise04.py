# 练习4：一张纸的厚度是0.01毫米，请问，对折多少次，可以超过珠穆朗玛峰8844.43米。
thickness = 1e-5
n = 0
while True:
    thickness *= 2;
    n += 1
    print(str(n) + "--" + str(thickness))
    if thickness > 8844.43:
        break
