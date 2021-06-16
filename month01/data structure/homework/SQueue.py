"""
    顺序队列

"""


class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self.__elem = []

    def is_empty(self):
        return not self.__elem

    def enqueue(self, value):
        self.__elem.append(value)

    def dequeue(self):
        if self.__elem:
            return self.__elem.pop(0)
        else:
            raise QueueError("Queue is empty.")

    def clear(self):
        self.__elem = []

    def get_length(self):
        return len(self.__elem)

if __name__ == "__main__":
    sq = SQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    sq.enqueue(3)
    print(sq.get_length())
    print(sq.dequeue())
    print(sq.dequeue())
    print(sq.get_length())