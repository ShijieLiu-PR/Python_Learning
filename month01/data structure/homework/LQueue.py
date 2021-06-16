"""
    链式队列
"""


class QueueError(Exception):
    pass


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LQueue:
    def __init__(self):
        self.head = self.rear = Node(None)

    def is_empty(self):
        return self.head == self.rear

    def enqueue(self, value):
        self.rear.next = Node(value)
        self.rear = self.rear.next

    def dequeue(self):
        if self.head != self.rear:
            self.head = self.head.next
            temp = self.head.value
            self.head.value = None
            return temp
        else:
            raise QueueError("Queue is empty.")

    def get_length(self):
        count = 0
        p = self.head
        while p != self.rear:
            count += 1
            p = p.next
        return count


if __name__ == "__main__":
    lq = LQueue()
    print(lq.is_empty())
    lq.enqueue(10)
    lq.enqueue(100)
    lq.enqueue(1000)
    print(lq.get_length())
    print(lq.dequeue())
    print(lq.get_length())
    print(lq.is_empty())
    print(lq.dequeue())
    print(lq.get_length())
    print(lq.is_empty())
    print(lq.dequeue())
    print(lq.get_length())

    print(lq.is_empty())