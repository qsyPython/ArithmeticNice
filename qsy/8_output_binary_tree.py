'''
    在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。
根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。
你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。
即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。
然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。
示例 1:

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]
示例 2:

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
示例 3:

输入:
      1
     / \
    2   5
   /
  3
 /
4
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
注意: 二叉树的高度在范围 [1, 10] 中。
'''

# 基础知识：
# 1、二叉树：有限个元素的集合，每个节点最多有两个子树的树结构。“左子树”和“右子树”。有左右之分，次序不能任意颠倒。
# 二叉排序树: 若左子树不空，则左子树上所有结点的值均小于它的根节点的值；
# 若右子树不空，则右子树上所有结点的值均大于它的根结点的值。
# 左、右子树也分别为二叉排序树
# 没有键值相等的节点
# 2、二重向量：行数为m 和 列数为n，实际上是2^节点数 -1

# 二叉树节点: 可根据节点闯将二叉树
class Node(object):
    def __init__(self,item):
        super(Node,self).__init__()
        self.item = item
        self.left_child = None
        self.right_child = None
    def __str__(self):
        return str(self.value)

# 二叉树类
class Tree(object):
    def __init__(self):
        super(Tree,self).__init__()
        self.root = None

    def add(self,item):
        '''添加节点'''
        node = Node(item)
        # 判断当前树是否为空
        if self.root is None:
            self.root = node
        else:
            queue =[]
            queue.append(self.root)
            # 采用队列存放, 先将根节点放入队列中,取出,看是否有左子树和右子树,有就放入并且循环回来看子树的子树,没有则添加
            while queue:
                temp = queue.pop(0)
                if temp.left_child is None:
                    temp.left_child = node
                    break
                elif temp.right_child is None:
                    temp.right_child = node
                    break
                # 都不为空,将左节点和右节点放入队列
                else:
                    queue.append(temp.left_child)
                    queue.append(temp.right_child)


    def wide_travel(self):
        '''深度遍历-广序遍历:从上到下,从左到右，利用队列'''
        if self.root is None:
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                temp = queue.pop(0)
                print(temp.item, end=" ")
                # 如果有左孩子则放入队列
                if temp.left_child is not None:
                    queue.append(temp.left_child)
                # 如果有右孩子则放入队列
                if temp.right_child is not None:
                    queue.append(temp.right_child)
            print()

    def preorder(self,node):
        '''深度遍历-先序遍历'''
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.left_child)
        self.preorder(node.right_child)

    def inorder(self, node):
        """深度遍历-中序遍历(左子树-根节点-右子树)"""
        if node is None:
            return
        self.inorder(node.left_child)
        print(node.item, end=" ")
        self.inorder(node.right_child)

    def posorder(self, node):
        """深度遍历-后序遍历(左子树-右子树-根节点)"""
        if node is None:
            return
        self.posorder(node.left_child)
        self.posorder(node.right_child)
        print(node.item, end=" ")

if __name__ == '__main__':
    tree = Tree()
    origin_list = ['A','B','C','D','E','F','G']
    for c in origin_list:
        tree.add(c)
    print("先序遍历:")
    tree.preorder(tree.root)
    print("\n中序遍历:")
    tree.inorder(tree.root)
    print("\n后序遍历:")
    tree.posorder(tree.root)
    print("\n广度遍历:")
    tree.wide_travel()