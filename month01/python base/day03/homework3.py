# 3. 一个球从100m的高度落下，每次回弹的高度为下落高度的一半，总共弹起多少次？（假定最小弹起高度为0.01m），总共弹了多少米？
height = 100.0
count = 0
distance = 0
while True:
    count += 1
    distance += (height + height/2)
    height = height / 2
    if height < 0.01:
        break
print("count = " + str(count))
print("distance = " + str(distance))