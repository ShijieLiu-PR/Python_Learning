"""
    链式栈
"""


class StackError(Exception):
    pass


# 创建节点类
class Node:
    """
        节点类
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LStack:
    def __init__(self):
        # 标记栈顶位置
        self.__top = None

    def is_empty(self):
        return self.__top is None

    def top(self):
        if self.__top is None:
            raise StackError("Stack is empty.")
        else:
            return self.__top.val

    def push(self, elem):
        self.__top = Node(elem, self.__top)

    def pop(self):
        elem = self.__top
        self.__top = self.__top.next
        return elem.val


if __name__ == "__main__":
    st = LStack()
    print(st.is_empty())

    st.push(20)
    st.push(30)
    st.push(40)
    print(st.pop())
    print(st.pop())
    print(st.top())

# 作业： 简单的加减法逆波兰表达式
        # 只包含加减法即可
        # p表示表达式的结束标志
        #