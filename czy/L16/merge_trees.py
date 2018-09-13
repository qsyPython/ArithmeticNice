
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
# 输入:
#  Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
#       3
#      / \
#     4   5
#    / \   \
#   5   4   7
# 注意: 合并必须从两个树的根节点开始


class Node(object):
    def __init__(self,data):
        self._data = data
        self._left = None
        self._right = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self, node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self, node):
        self._right = node

    def get_right(self):
        return self._right

#按层读取节点
a = []
def getTreeHeight(root = Node):
    if not root is None:
        leftHeight = getTreeHeight(root.get_left())
        rightHeight = getTreeHeight(root.get_right())
        return max(leftHeight,rightHeight) + 1
    else:
        return 0

def printNodeAtLevel(root,level):
    if (not root is None):
        if level == 0:
            a.append(root.get_data())
        else:
            printNodeAtLevel(root.get_left(),level -1)
            printNodeAtLevel(root.get_right(), level - 1)

    else:
        if level == 0:
            a.append(None)

def levelOrder(root = Node):
    if (not root is None):
        totalLevel = getTreeHeight(root)
        for i in range(totalLevel):
            printNodeAtLevel(root,i)

def arrayToBiTree(array):
    if (not array is None) or len(array) == 0:
        length = len(array)
        #创建数据结构体
        pRoot = []
        for i in range(length):
            pRoot.append(Node(None))
            pRoot[i].set_data(array[i])
            pRoot[i].set_left(None)
            pRoot[i].set_right(None)
        #父节点与左右孩子关联 length/2 - 1 是深度
        for k in range(int(length/2)):
            if 2*k + 1 < length:
                pRoot[k].set_left(pRoot[2 * k + 1])
            if 2*k + 2 < length:
                pRoot[k].set_right(pRoot[2 * k + 2])

    return pRoot
#合并数组
def mergeTrees(n1 = Node,n2 = Node):
    if (n1 is None) and (n2 is None):
        return None
    if n1 is None:
        return n2
    if n2 is None:
        return n1

    if (not n1.get_data() is None) and (not n2.get_data() is None):
        n1.set_data(n1.get_data() + n2.get_data())
    elif n1.get_data() is None:
        n1.set_data(n2.get_data())

    n1.set_right(mergeTrees(n1.get_right(),n2.get_right()))
    n1.set_left(mergeTrees(n1.get_left(), n2.get_left()))

    return n1


if __name__ == '__main__':
    tree_1 = [1, 3, 2, 5, None,None,None]
    tree_2 = [2, 1, 3,None, 4, None, 7]
    node_array_1 = arrayToBiTree(tree_1)
    node_array_2 = arrayToBiTree(tree_2)
    print(tree_1)
    print(tree_2)
    node = mergeTrees(node_array_1[0],node_array_2[0])
    levelOrder(node)
    print(a)

