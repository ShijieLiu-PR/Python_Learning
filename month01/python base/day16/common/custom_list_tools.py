"""
    针对列表的自定义工具
"""


class ListHelper:
    @staticmethod
    def find_all(target, func_condition):
        """
            查找列表中满足条件的所有元素
        :param target: 列表
        :param func_condition: 条件
            函数/方法类型
            参数：列表中的元素
            返回值：是否满足条件bool值
        :return:
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target, func):
        """
            筛选指定列表中满足条件的元素。
        :param target:
        :param func:
        :return:
        """
        for item in target:
            yield func(item)

    @staticmethod
    def sum(target, func):
        res = 0
        for item in target:
            res += func(item)
        return res

    @staticmethod
    def last_match(target, func):
        result = None
        for item in target:
            if func(item):
                result = item
        return result

    @staticmethod
    def last(target, func):
        for i in range(len(target), -1, -1):
            if func(target[i]):
                return target[i]

    @staticmethod
    def exist(target, func):
        for item in target:
            if func(item):
                return True
        return False

    @staticmethod
    def delete(target, func):
        for i in range(len(target) - 1, -1, -1):
            print(i)
            if func(target[i]):
                del target[i]

    @staticmethod
    def get_max(target, func):
        result = target[0]
        for i in range(1, len(target)):
            if func(result) < func(target[i]):
                result = target[i]
        return result

    @staticmethod
    def get_min(target, func):
        result = target[0]
        for i in range(1, len(target)):
            if func(result) > func(target[i]):
                result = target[i]
        return result

    @staticmethod
    def ascend(target, func):
        for i in range(len(target) - 1):
            for j in range(i+1, len(target)):
                if func(target[i]) > func(target[j]):
                    target[i], target[j] = target[j], target[i]
        return target

    @staticmethod
    def descend(target, func):
        for i in range(len(target) - 1):
            for j in range(i+1, len(target)):
                if func(target[i]) < func(target[j]):
                    target[i], target[j] = target[j], target[i]
        return target

    @staticmethod
    def sort(target, func):
        """
            万能排序
        :param target: 需要排序的数据
        :param func: 排序的逻辑
               func类型是函数
               参数列表中两个元素
               返回值是比较结果
               方法是比较条件
        :return:
        """
        for i in range(len(target)-1):
            for j in range(i, len(target)):
                if func(target[i], target[j]):
                    target[i], target[j] = target[j], target[i]
        return target
