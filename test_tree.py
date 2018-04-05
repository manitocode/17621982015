# 树的实现需要多学习！

class Node(object):
    """docstring for Node"""

    def __init__(self, index):
        self.index = index
        self.left_child = None
        self.right_child = None


class Tree(object):

    def __init__(self,root):
        self.root = root

    def pre_(self,node):
        if not node:
            return
        print(node.index)
        self.pre_(node.left_child)
        self.pre_(node.right_child)

node_dict = {}
for i in range(1, 10):
    node_dict[i] = Node(i)
node_dict[1].left_child = node_dict[2]
node_dict[1].right_child = node_dict[3]
node_dict[2].left_child = node_dict[5]
node_dict[2].right_child = node_dict[6]
node_dict[3].left_child = node_dict[7]
node_dict[7].left_child = node_dict[8]
node_dict[7].right_child = node_dict[9]

tree = Tree(node_dict[1])
tree.pre_(tree.root)