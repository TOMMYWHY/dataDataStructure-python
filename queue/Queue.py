# coding:utf-8


class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)
        #self.__list.insert(0,item)

    def dequeue(self):
        return self.__list.pop(0)
        # self.__list.pop()

    def is_empty(self):
        return self.__list ==[]

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(11)
    s.enqueue(12)
    s.enqueue(13)
    s.enqueue(14)

    print(s.is_empty())
    print(s.size())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
