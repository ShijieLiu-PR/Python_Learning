
# 创建节点类
class Node:
    """
        节点类
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链表的操作
class LinkList:
    def __init__(self):
        self.head = None

    # 初始化链表元素
    def init_list(self, l):
        self.head = Node(None)
        p = self.head
        for i in l:
            p.next = Node(i)
            p = p.next

    # 打印链表元素
    def show(self):
        p = self.head.next
        while p:
            print(p.val)
            p = p.next

    # 在链表尾部插入一个元素
    def append(self, value):
        p = self.head.next
        while p.next:
            p = p.next
        p.next = Node(value)

    # 获得链表元素长度
    def get_length(self):
        p = self.head.next
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    # 判断链表是否为空
    def is_empty(self):
        return self.get_length() == 0

    # 清除链表
    def clear(self):
        self.head.next = None

    # 根据索引取出元素
    def get_item(self, index):
        p = self.head.next
        while p and index != 0:
            p = p.next
            index -= 1
        if index == 0:
            return p.val
        else:
            raise IndexError("Index is out of range.")

    # 在指定所引出插入元素
    def insert(self, index, item):
        p = self.head
        i = -1
        while p:
            if i + 1 == index:
                break
            else:
                p = p.next
                i += 1
        if p is None:
            raise IndexError("Index is out of range.")
        else:
            remaining = p.next
            p.next = Node(item)
            p = p.next
            p.next = remaining

    # 删除链表中的第一个元素
    def delete(self, item):
        p = self.head
        while p.next:
            if item == p.next.val:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("%s is not in list." % item.__str__())

if __name__ == "__main__":
    # 创建链表对象
    link = LinkList()

    # 初始数据
    l = [1, "abc", (2,3), 4, 5, 6]
    link.init_list(l)
    link.delete(1)
    link.show()
