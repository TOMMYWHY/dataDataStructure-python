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

    def breadth_first_traversal(self):
        """广度优先"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)

    # 深度遍历  先序遍历 中序遍历 后续遍历 # 根节点位置

    def preoder(self,node):
        if node is None:
            return
        print(node.elem, end=" ")
        self.preoder(node.l_child)
        self.preoder(node.r_child)

    def inoder(self,node):
        if node is None:
            return
        self.inoder(node.l_child)
        print(node.elem, end=" ")
        self.inoder(node.r_child)

    def postoder(self,node):
        if node is None:
            return
        self.postoder(node.l_child)
        self.postoder(node.r_child)
        print(node.elem, end=" ")



if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)

    tree.breadth_first_traversal()
    print()
    print("----先序遍历----")
    tree.preoder(tree.root)
    print()

    print("----中序遍历----")
    tree.inoder(tree.root)
    print()

    print("----后续遍历----")
    tree.postoder(tree.root)
