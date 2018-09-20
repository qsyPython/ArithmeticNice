# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，
# 使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。
#
# 示例 1:
#
# 输入:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# 输出:
#     1
#       \
#        2
# 示例 2:
#
# 输入:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# 输出:
#       3
#      /
#    2
#   /
#  1
# 解题思路：
#
# 二叉搜索树的裁剪，从根节点开始，若根节点在裁剪范围左侧，
# 那么他和他的左子树完全裁剪；若根节点在裁剪范围右侧，那么他和他的右子树完全裁剪；
# 若根节点在裁剪范围（不用裁剪），按照递归分别推出他左右子树的裁剪结果。
class treeNode():
    def __init__(self, data=None):
        self._data = data;
        self._left = None;
        self._right = None;

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
def getTreeHeight(root = treeNode):
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


def levelOrder(root = treeNode):
    if (not root is None):
        totalLevel = getTreeHeight(root)
        for i in range(totalLevel):
            printNodeAtLevel(root,i)
#修剪节点
def trimBinaryTree(node = treeNode,L = int,R = int):
    if node is None:
        return None
    if node.get_data() < L:
        return trimBinaryTree(node.get_right(),L,R)
    elif node.get_data() > R:
        return trimBinaryTree(node.get_left(), L, R)
    else:
        node.set_left(trimBinaryTree(node.get_left(), L, R))
        node.set_right(trimBinaryTree(node.get_right(), L, R))

    return node

#数组转节点
def arrayToBiTree(array):
    if (not array is None) or len(array) == 0:
        length = len(array)
        #创建数据结构体
        pRoot = []
        for i in range(length):
            pRoot.append(treeNode())
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


if __name__ == '__main__':

    array = [1,0,2,3,6,4]
    pNodes =  arrayToBiTree(array)
    pNode = trimBinaryTree(pNodes[0],1,5)
    levelOrder(pNodes[0])
    print(a)