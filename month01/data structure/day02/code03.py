"""
    链式队列
"""


class QueueError(Exception):
    pass


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkQueue:
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return not self.head and not self.rear

    def get_length(self):
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.next
        return count

    def enqueue(self, value):
        if self.is_empty():
            self.head = self.rear = Node(value)
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")
        else:
            temp = self.head.value
            self.head = self.head.next
            if not self.head:
                self.rear = None
            return temp


if __name__ == "__main__":
    lq = LinkQueue()
    print(lq.is_empty())
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    print(lq.dequeue())
    print(lq.is_empty())
    print(lq.dequeue())
    print(lq.is_empty())
    lq.enqueue(5)
    lq.enqueue(6)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())

