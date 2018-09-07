# 给定二叉树根结点
# root ，此外树的每个结点的值要么是
# 0，要么是
# 1。
#
# 返回移除了所有不包含
# 1
# 的子树的原二叉树。
#
# (节点 X 的子树为 X 本身，以及所有 X 的后代。)
#
# 示例1:
# 输入: [1, null, 0, 0, 1]
# 输出: [1, null, 0, null, 1]
#
# 解释:
# 只有红色节点满足条件“所有不包含
# 1
# 的子树”。
# 右图为返回的答案。
#
#
# 示例2:
# 输入: [1, 0, 1, 0, 0, 0, 1]
# 输出: [1, null, 1, null, 1]
#
# 示例3:
# 输入: [1, 1, 0, 1, 1, 0, 1, 0]
# 输出: [1, 1, 0, 1, 1, null, 1]
#
# 说明:
#
# 给定的二叉树最多有
# 100
# 个节点。
# 每个节点的值只会为
# 0
# 或
# 1 。

#节点类
class Node(object):
    def __init__(self,data = None):
        self._data = data
        self._left = None
        self._right = None
        self._arrayOrder = None

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

    def set_arrayOrder(self, node):
        self._arrayOrder = node

#数组转换成节点
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
            pRoot[i].set_arrayOrder(i)
        #父节点与左右孩子关联 length/2 - 1 是深度
        for k in range(int(length/2)):
            if 2*k + 1 < length:
                pRoot[k].set_left(pRoot[2 * k + 1])
            if 2*k + 2 < length:
                pRoot[k].set_right(pRoot[2 * k + 2])

    return pRoot

#减掉为了0的子节点
def pruneTree(root = Node):
    if not root is None:
        root.set_left(pruneTree(root.get_left()))
        root.set_right(pruneTree(root.get_right()))
        if (root.get_left() is None) and (root.get_right() is None) and (root.get_data() == 0):
            return None
        else:
            return root

    return None
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

if __name__ == '__main__':
        # 实例化根节点 [4, 2, 7, 1, 3, 6, 9]
        #数组转化成节点数组
        array = [1, 1, 0, 1, 1, 0, 1, 0]
        print(array)
        list = arrayToBiTree(array)
        root = pruneTree(list[0])
        levelOrder(root)
        print(a)  #[1, 1, 0, 1, 1, None, 1]




