"""
    队列
    线性结构
"""


class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self.__elem = []

    def is_emtpy(self):
        return self.__elem == []

    def clear(self):
        self.__elem = []

    def get_length(self):
        return len(self.__elem)

    def enqueue(self, value):
        self.__elem.append(value)

    def dequeue(self):
        if self.__elem:
            return self.__elem.pop(0)
        else:
            raise QueueError("SQueue is empty.")


if __name__ == "__main__":
    queue = SQueue()
    print(queue.is_emtpy())
    queue.enqueue(11)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    list01 = ["a","b", "c"]
