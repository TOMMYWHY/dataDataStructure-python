class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count = count + 1
        return count

    def traverse(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node  # 添加 node 的下一个 的 前驱 = 要添加的 node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):

        if pos <= 0:
           self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count = count + 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.__head

        while cur is not None:
            if cur.item is item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None  # 判断 尽一个节点
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
        # if :

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item is item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(11)
    print(dll.is_empty())
    print(dll.length())

    dll.append(22)
    dll.append(33)
    dll.append(44)
    dll.append(55)
    dll.traverse()

    dll.add(100)
    dll.traverse()

    dll.insert(-1, 9)
    dll.insert(3, 99)
    dll.insert(11, 999)
    dll.traverse()

    dll.remove(9)
    dll.traverse()

    dll.remove(100)
    dll.traverse()
    dll.remove(44)
    dll.traverse()
