class Node(object):
    def __init__(self, item):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = []  # 用于遍历
        queue.append(self.root)

        while queue:
            cur_node = queue.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)  # 节点不为空时 添入遍历队列
            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)
