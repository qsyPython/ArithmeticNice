# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
#
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
#
# Example 1:
#
# 输入: [3,2,1,6,0,5]
# 输入: 返回下面这棵树的根节点：
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# 注意:
#
# 给定的数组的大小在 [1, 1000] 之间。
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

def constructMaximumBinaryTree(arr_num ):
    if (arr_num is None) or len(arr_num) <= 0:
        return None
    elif(len(arr_num) == 1):
        return  Node(arr_num[0])
    elif(len(arr_num) < 1000):
        max = 0
        length = len(arr_num)
        for i in range(length):
            if arr_num[i] > arr_num[max]:
                max = i
        left_num = []
        right_num = []

        for j in range(max):
            left_num.append(arr_num[j])

        for k in range(max+ 1,length):
            right_num.append(arr_num[k])

        node = Node(arr_num[max])

        node.set_left(constructMaximumBinaryTree(left_num))
        node.set_right(constructMaximumBinaryTree(right_num))
        return node
    else:
        return None



#*********按层读取节点************
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
#********************* end *********************

if __name__ == '__main__':
    arr_num = [3,2,1,6,0,5]
    node = constructMaximumBinaryTree(arr_num);
    print(arr_num)
    levelOrder(node)
    print(a)







