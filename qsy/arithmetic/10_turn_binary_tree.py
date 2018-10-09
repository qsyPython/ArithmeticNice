'''
    翻转二叉树: 这个题 homebrew 的编写者曾经面试google时，不会做，因此被拒
    翻转一棵二叉树。
示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class Node(object):
    def __init__(self,item):
        super(Node,self).__init__()
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.item)

class Tree(object):
    def __init__(self):
        super(Tree,self).__init__()
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
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
        return  result

    # 翻转二叉树：根据root递归获取到left和right分支；然后对左右分支进行交换
    def turn_tree(self,root):
        if root is not None:
            # 递归二叉树的左右子树
            root.left = self.turn_tree(root.left)
            root.right = self.turn_tree(root.right)

            # 将左右子树交换
            tmp = root.left
            root.left = root.right
            root.right = tmp
        return root

if __name__ == '__main__':
    list = [1,None,3,5,7,9]
    tree = Tree()
    [tree.add(item) for item in list]
    tree.turn_tree(tree.root)
    result_list = tree.wide_travel()
    print('查看翻转二叉树的最终结果：%s' % result_list)



