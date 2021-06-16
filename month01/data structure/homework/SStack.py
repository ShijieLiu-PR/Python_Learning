"""
    顺序栈
"""


class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        self.__elem = []

    def is_emtpy(self):
        return not self.__elem

    def clear(self):
        self.__elem = []

    def top(self):
        if self.__elem:
            return self.__elem[-1]
        else:
            raise StackError("Stack is empty.")

    def push(self, value):
        self.__elem.append(value)

    def pop(self):
        if self.__elem:
            return self.__elem.pop()
        else:
            raise StackError("Stack is empty.")

    def get_length(self):
        return len(self.__elem)


if __name__ == "__main__":
    ss = SStack()
    print(ss.is_emtpy())
    ss.push(1)
    ss.push(2)
    ss.push(3)
    print(ss.get_length())
    print(ss.pop())
    print(ss.pop())
    print(ss.pop())