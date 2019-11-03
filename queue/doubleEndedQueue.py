class DoubleEndedQueue(object):

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0,item)

    def add_rear(self,item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)
        # self.__list.pop()

    def pop_rear(self):
        return  self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = DoubleEndedQueue()
    s.add_front(11)
    s.add_front(12)
    s.add_front(13)
    s.add_front(14)

    print(s.is_empty())
    print(s.size())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())
