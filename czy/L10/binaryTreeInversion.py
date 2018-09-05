# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

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

#前序遍历
def arrayPrePrint(array = list,root = Node):
    if (not array is  None) and (not root is None):
        array.append(root.get_data())
        arrayPrePrint(array,root.get_left())
        arrayPrePrint(array,root.get_right())

def inversion(root = Node):
    if (not root) or ((not root.get_left()) and (not root.get_right())) :
        return root
    else:
      tempNode = root.get_left();
      root.set_left(inversion(root.get_right()))
      root.set_right(inversion(tempNode))
    return root


if __name__ == '__main__':
        # 实例化根节点 [4, 2, 7, 1, 3, 6, 9]
        #数组转化成节点数组
        array = [4, 2, 7, 1, 3, 6, 9]
        print(array)
        list = arrayToBiTree(array)
        #前序读取
        pArray = []
        arrayPrePrint(pArray, list[0])
        print(pArray)   # [4, 2, 1, 3, 7, 6, 9]
        #反转节点
        pArray= []
        rootList = inversion(list[0])
        arrayPrePrint(pArray, rootList)
        print(pArray)  #[4, 7, 9, 6, 2, 3, 1]

