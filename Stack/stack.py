# coding:utf-8

class Stack(object):
    def __init__(self):
        self.__list = []
        # 尾部 为栈顶

    def push(self,item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list: # 判断是否为空
            return self.__list[len(self.__list)-1]
            # return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []
        #return not self.__lsit

    def size(self):
        return len(self.__list)



if __name__ == "__main__":
    s = Stack()
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    print(s.peek())
    print(s.is_empty())
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
