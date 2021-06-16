from code03 import *


def calculate(input_str):
    for item in input_str.split():
        yield item


if __name__ == "__main__":
    st = LStack()
    while True:
        for item in calculate(input("请输入公式：")):
            if item.isnumeric():
                st.push(int(item))
            elif item == "+":
                item1 = st.pop()
                item2 = st.pop()
                st.push(item2 + item1)
            elif item == "-":
                item1 = st.pop()
                item2 = st.pop()
                st.push(item2 - item1)
            else:
                print(st.pop())
