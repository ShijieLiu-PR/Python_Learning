"""
    线性链式表
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LList:
    def __init__(self):
        self.__head = Node(None)

    def is_empty(self):
        return not self.__head.next

    def get_length(self):
        count = 0
        p = self.__head.next
        while p:
            count += 1
            p = p.next
        return count

    def append(self, value):
        p = self.__head
        while p.next:
            p = p.next
        p.next = Node(value)

    def get_item(self, index):
        p = self.__head.next
        while p:
            if index == 0:
                break
            else:
                index -= 1
                p = p.next
        if not p:
            raise IndexError("Index is out of range.")
        else:
            return p.value

    def insert(self, index, value):
        p = self.__head
        prior = self.__head
        count = -1
        while p:
            count += 1
            prior = p
            p = p.next
            if index == count:
                prior.next = Node(value, p)
                break
        if index != count:
            raise IndexError("Index is out of range.")

    def show(self):
        res = []
        p = self.__head.next
        while p:
            res.append(p.value)
            p = p.next
        print(res)

    def clear(self):
        self.__head.next = None

    def delete(self, value):
        p = self.__head.next
        prior = self.__head
        while p:
            if p.value == value:
                prior.next = p.next
                break
            else:
                prior = p
                p = p.next


if __name__ == "__main__":
    ll = LList()
    print(ll.is_empty())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.is_empty())
    print(ll.get_length())
    ll.show()
    ll.insert(0,"a")
    ll.show()
    ll.delete(3)
    ll.show()

