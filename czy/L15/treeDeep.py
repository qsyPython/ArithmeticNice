# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3
class Node(object):
    def __init__(self,data = None):
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

def arrayToBiTree(array):
    if (not array is None) or len(array) == 0:
        length = len(array)
        #创建数据结构体
        pRoot = []
        for i in range(length):
            pRoot.append(Node())
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

def getTreeHeight(root = Node):
    if not root is None:
        leftHeight = getTreeHeight(root.get_left())
        rightHeight = getTreeHeight(root.get_right())
        return max(leftHeight,rightHeight) + 1
    else:
        return 0

if __name__ == '__main__':
    arr_num = [3,2,1,6,0,5]
    nodeArray = arrayToBiTree(arr_num)
    print(getTreeHeight(nodeArray[0]))
