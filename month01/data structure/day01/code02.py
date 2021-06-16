"""
    栈的顺序存储结构
    重点代码
"""


# 自定义栈异常
class StackError(Exception):
    pass


# 基于列表实现顺序栈
class SStack:
    def __init__(self):
        # 约定列表的最后一个元素为栈顶
        self._elems = []

    def top(self):
        if not self._elems:
            raise StackError("stack is empty.")
        else:
            return self._elems[-1]

    # 判断栈是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, elem):
        self._elems.append(elem)

    # 出栈
    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()


def match(str):
    st = SStack()
    left = ("(", "[", "{")
    right = (")", "]", "}")
    for c in str:
        if c in left:
            st.push(c)
        elif c in right:
            if left.index(st.pop()) != right.index(c):
                return "fail"
    return "pass"



if __name__ == "__main__":
    st = SStack()
    st.push(20)
    st.push(30)
    st.push(40)
    while not st.is_empty():
        print(st.pop())
    str = "4234(ffa)faff{dfe}[999)]ffaa"
    print(match(str))
# 练习1：检测一段文字中的括号是否为成对出现，如果不是，则报出括号匹配的错误问题。
