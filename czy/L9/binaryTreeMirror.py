# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#判断一棵二叉树本身是否是镜像对称的，这个问题可以转化为：二叉树的左子树与右子树是否是镜像对称的。
# 本题的解法同样有递归和迭代两种方法：
# （设二叉树左子树为leftN，右子树为rightN，leftN、rightN均指向左右子树的根）
# 递归：leftN和rightN的值相等，并且leftN的左子树与rightN的右子树对称，leftN的右子树与rightN的左子树对称
#
# 迭代：维护一个栈，方法与上一篇文章中判断二叉树是否相等类似，
# 只不过，我们在将节点入栈的时候，顺序不是     leftN->left , rightN->left ,leftN->right ,rightN->right，
# 而是leftN->left , rightN->right , leftN->right ,rightN->left，为什么？因为我们要判断的是对称，
# 所以leftN->left 对应rightN->right，leftN->right 对应rightN->left，它们的入栈顺序理应如此。
class Node():
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

#递归
#判断两个节点是否对称递归函数
def symmetric(leftN = Node,rightN = Node):
    if (not leftN) and (not rightN):
        return True
    if (not leftN) or (not rightN):
        return False
    return  (leftN.get_data() == rightN.get_data()) and symmetric(leftN.get_left(),rightN.get_right()) and symmetric(leftN.get_right(),rightN.get_left())

#是否对称启动函数
def isSymmetric(root = Node):
    if not root:
        return  True
    return symmetric(root.get_left(),root.get_right())

#通过迭代判断
#定义一个栈
class Stack(object):
    """栈"""
    def __init__(self):
         self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        """加入元素"""
        self.items.append(item)

    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的大小"""
        return len(self.items)

def isSymmetric(root = Node):
    if not root:
        return True
    s= Stack()
    leftN = root.get_left()
    rightN = root.get_right()

    s.push(leftN)
    s.push(rightN)

    while not s.is_empty():
        leftN = s.peek()
        s.pop()

        rightN = s.peek()
        s.pop()

        if (not leftN) and (not rightN):
            continue
        if (not leftN) or (not rightN):
            return False
        if leftN.get_data() != rightN.get_data():
            return False

        s.push(leftN.get_left())
        s.push(rightN.get_right())
        s.push(leftN.get_right())
        s.push(rightN.get_left())

    return True

if __name__ == '__main__':

    # 实例化根节点 [1,2,2,3,4,4,3]
    root_node = Node(1)
    left_node = Node(2)
    left_node_1 = Node(3)
    right_node_1 = Node(4)
    left_node.set_left(left_node_1)
    left_node.set_right(right_node_1)
    right_node = Node(2)
    left_node_2 = Node(4)
    right_node_3 = Node(3)
    right_node.set_left(left_node_2)
    right_node.set_right(right_node_3)
    root_node.set_left(left_node)
    root_node.set_right(right_node)


    print(isSymmetric(root_node))

