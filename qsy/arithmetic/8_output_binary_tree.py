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

输入: m2 n3
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
# 思路 -> 二重向量：行数为m为深度 和 列数为n为，实际上是2^节点数 -1

# # 二叉树节点: 可根据节点创建二叉树
# class Node(object):
#     def __init__(self,item):
#         super(Node,self).__init__()
#         self.item = item
#         self.left_child = None
#         self.right_child = None
#     def __str__(self):
#         return str(self.value)
#
# # 二叉树类
# class Tree(object):
#     def __init__(self):
#         super(Tree,self).__init__()
#         self.root = None
#
#     def add(self,item):
#         '''添加节点'''
#         node = Node(item)
#         # 判断当前树是否为空
#         if self.root is None:
#             self.root = node
#         else:
#             queue =[]
#             queue.append(self.root)
#             # 采用队列存放, 先将根节点放入队列中,取出,看是否有左子树和右子树,有就放入并且循环回来看子树的子树,没有则添加
#             while queue:
#                 temp = queue.pop(0)
#                 if temp.left_child is None:
#                     temp.left_child = node
#                     break
#                 elif temp.right_child is None:
#                     temp.right_child = node
#                     break
#                 # 都不为空,将左节点和右节点放入队列
#                 else:
#                     queue.append(temp.left_child)
#                     queue.append(temp.right_child)
# #
# #
#     def wide_travel(self):
#         '''深度遍历-广序遍历:从上到下,从左到右，利用队列'''
#         if self.root is None:
#             return
#         else:
#             queue = []
#             queue.append(self.root)
#             while queue:
#                 temp = queue.pop(0)
#                 print('广序排序：%s' % temp.item, end=" ")
#                 # 如果有左孩子则放入队列
#                 if temp.left_child is not None:
#                     queue.append(temp.left_child)
#                 # 如果有右孩子则放入队列
#                 if temp.right_child is not None:
#                     queue.append(temp.right_child)
# #
# #
#     def preorder(self,node):
#         '''深度遍历-先序遍历'''
#         if node is None:
#             return
#         print(node.item, end=" ")
#         self.preorder(node.left_child)
#         self.preorder(node.right_child)
#
#     def inorder(self, node):
#         """深度遍历-中序遍历(左子树-根节点-右子树)"""
#         if node is None:
#             return
#         self.inorder(node.left_child)
#         print(node.item, end=" ")
#         self.inorder(node.right_child)
#
#     def posorder(self, node):
#         """深度遍历-后序遍历(左子树-右子树-根节点)"""
#         if node is None:
#             return
#         self.posorder(node.left_child)
#         self.posorder(node.right_child)
#         print(node.item, end=" ")
# #
# if __name__ == '__main__':
#     tree = Tree()
#     origin_list = ['A','B','C','D','E','F','G']
#     for c in origin_list:
#         tree.add(c)
#     print("先序遍历:") # A B D E C F G
#     tree.preorder(tree.root)
#     print("\n中序遍历:") # D B E A F C G
#     tree.inorder(tree.root)
#     print("\n后序遍历:") # D E B F G C A
#     tree.posorder(tree.root)
#     print("\n广度遍历:") # A B C D E F G
#     tree.wide_travel()

# 定义二叉树节点
class Node(object):
    def __init__(self,item):
        super(Node, self).__init__()
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.item)

# 定义二叉树类：包括添加节点
class Tree(object):
    def __init__(self):
        super(Tree,self).__init__()
        self.root = None

    def add(self,item):
        ''' 添加节点 '''
        node = Node(item)
        # 判断当前树根是否为空
        if self.root is None:
            self.root = node
        else:
            queue =[]
            queue.append(self.root)
            # 采用队列存放, 先将根节点放入队列中,取出,看是否有左子树和右子树,有就放入并且循环回来看子树的子树,没有则添加
            while queue:
                temp = queue.pop(0)
                if temp.left is None:
                    temp.left = node
                    break
                elif temp.right is None:
                    temp.right = node
                    break
                else:
                    # 都不为空,将左节点和右节点放入队列!!! #少：修正同时处理异常null时list情况
                    if temp.left.item is not None:
                        queue.append(temp.left)
                    if temp.right.item is not None:
                        queue.append(temp.right)

    def wide_travel(self):
        result = []
        if self.root is not None:
            queue = []
            queue.append(self.root)
            while queue:
                temp = queue.pop(0)
                result.append(temp.item)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
        return result

# 处理二叉树的root
class Solution(object):
    def print_tree(self,root):

        # 获取二叉树所处深度
        def depth(root):
            if root and root.item is not None: #少：修正异常二叉树的情况 -> root 存在; 且root.item不为空
                return max(depth(root.left),depth(root.right))+1
            else:
                return 0

        height = depth(root)
        width = pow(2,height)-1
        # 初始化 返回结果
        res = [["" for j in range(width)] for i in range(height)]

        # 打印树: res为待修改的结果；root为当前节点；h为当前节点的处在的列；pos为所在的位置
        def print_tree(res,root,h,pos):
            if root and root.item is not None: #少：修正异常二叉树的情况 -> root 存在; 且root.item不为空
                # 修改res
                res[h-1][pos] = '%d' % root.item
                step = pow(2,height-h-1)
                print_tree(res,root.left,h+1,pos-step)
                print_tree(res,root.right,h+1,pos+step)
        print_tree(res,root,1,int(width/2))

        return res

if __name__ == '__main__':
    origin_list = [1,None,2,5]
    tree = Tree()
    [tree.add(item) for item in origin_list]
    s = Solution()
    result = s.print_tree(tree.root)
    print(result)




