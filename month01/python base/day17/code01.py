"""
    day 16 复习
"""
import sys
list01 = [5, 8, 0, 4, 1]


def fun01(target):
    result = list()
    for item in target:
        if item > 5:
            result.append(item)
    return result


# def fun02(target):
#     for item in target:
#         if item > 5:
#             yield item

class MyIterator:
    def __init__(self, target):
        self.index = 0
        self.target = target

    def __iter__(self):
        return self

    def __next__(self):
        result = None
        if self.index < len(self.target):
            result = self.target[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# gen = MyIterator(list01)
# result02 = []
# while True:
#     try:
#         res = gen.__next__()
#         result02.append(res)
#     except:
#         break
for item in MyIterator(list01):
    print(item)
result01 = fun01(list01)
# result02 = fun02(list01)
print(result01)
print(sys.path)