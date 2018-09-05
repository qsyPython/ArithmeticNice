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
                    if temp.left.item is not '':
                        queue.append(temp.left)
                    if temp.right.item is not '':
                        queue.append(temp.right)
    def turn_tree(self,root):
        if root is None:
            return root
        # 递归二叉树的左右子树
        root.left = self.turn_tree(root.left)
        root.right = self.turn_tree(root.right)
        # 将左右子树交换
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root

if __name__ == '__main__':
    tree = Tree()
    list = [1,3,5,7,'',9]
    for item in list:
        tree.add(item)
    new_root = tree.turn_tree(tree.root)



