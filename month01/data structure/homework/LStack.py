"""
    链式栈
"""


class StackError(Exception):
    pass


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LStack:
    def __init__(self):
        self.__top = None

    def is_empty(self):
        return not self.__top

    def push(self, value):
        if self.__top:
            self.__top = Node(value, self.__top)
        else:
            self.__top = Node(value, None)

    def pop(self):
        if self.__top:
            value = self.__top.value
            self.__top = self.__top.next
            return value
        else:
            raise StackError("Stack is empty.")

    def get_length(self):
        count = 0
        p = self.__top
        while p:
            count += 1
            p = p.next
        return count


if __name__ == "__main__":
    ss = LStack()
    print(ss.is_empty())
    ss.push(1)
    ss.push(2)
    ss.push(3)
    # print(ss.get_length())
    print(ss.pop())
    print(ss.get_length())
    print(ss.pop())
    print(ss.get_length())
    print(ss.pop())
    print(ss.get_length())



