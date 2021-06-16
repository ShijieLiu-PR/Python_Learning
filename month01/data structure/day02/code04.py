"""
    链式队列：采用站位空节点的方式
    重点代码
"""


class QueueError(Exception):
    pass


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LQueue:
    def __init__(self):
        self.head = self.rear = Node(None)

    def is_empty(self):
        return self.head == self.rear

    def get_length(self):
        count = 0
        p = self.head
        while p != self.rear:
            count += 1
            p = p.next
        return count

    def enqueue(self, value):
        self.rear.next = Node(value)
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")
        else:
            self.head = self.head.next
            return self.head.value

    def clear(self):
        self.head = self.rear


if __name__ == "__main__":
    lq = LQueue()
    print(lq.is_empty())
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    print(lq.get_length())
    print(lq.dequeue())
    print(lq.is_empty())
    lq.clear()
    print(lq.is_empty())

