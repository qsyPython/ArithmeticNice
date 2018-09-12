'''
    二叉树的最大深度：
    给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

class Node(object):
    def __init__(self,item):
        super(Node,self).__init__()
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return  str(self.item)
    __repr__ = __str__

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

    def depth(self,root):
        if root and root.item is not None:
            return max(self.depth(root.left),self.depth(root.right)) + 1
        else:
            return 0
    # 计算数的最大深度
    def depth(self,root):
        if root and root.item is not None:
            return max(self.depth(root.left),self.depth(root.right)) + 1
        else:
            return  0

if __name__ == '__main__':
    origin_list = [3,9,20,None,None,15,7]
    tree = Tree()
    [tree.add(item) for item in origin_list]
    max_depth = tree.depth(tree.root)
    print(max_depth)