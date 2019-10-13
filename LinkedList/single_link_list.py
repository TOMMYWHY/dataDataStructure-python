class Node(object):
    """node"""

    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkList(object):
    """list"""

    def __init__(self, node=None):
        self.__head = node
        pass

    def is_empty(self):
        return self.__head is None

    def length(self):
        current = self.__head
        count = 0
        while current != None:
            current = current.next
            count += 1
        return count

    def traverse(self):
        current = self.__head
        while current != None:
            print(current.element, end=", ")
            current = current.next
        print()

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.__head
        self.__head = new_node

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.__head = new_node
        else:
            current = self.__head
            while current.next != None:
                current = current.next
            current.next = new_node

    def insert(self, position, item):
        """
        :param position: from 0
        :param item:
        :return:
        """
        if position < 0:
            self.add(item)
        elif position > self.length() - 1:
            self.append(item)
        else:
            new_node = Node(item)
            pre = self.__head
            count = 0
            while count < (position - 1):
                pre = pre.next
                count += 1
            new_node.next = pre.next
            pre.next = new_node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.element == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        current = self.__head
        while current != None:
            if current.element == item:
                return True
            else:
                current = current.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(11)
    print(ll.is_empty())
    print(ll.length())

    ll.append(22)
    ll.append(33)
    ll.append(44)
    ll.append(55)
    ll.traverse()

    ll.add(100)
    ll.traverse()

    ll.insert(-1, 9)
    ll.insert(3, 99)
    ll.insert(11, 999)
    ll.traverse()

    ll.remove(9)
    ll.traverse()

    ll.remove(100)
    ll.traverse()
    ll.remove(44)
    ll.traverse()
