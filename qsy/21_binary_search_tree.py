'''
    修剪二叉搜索树:
    给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例 1:
输入:
    1
   / \
  0   2

  L = 1
  R = 2

输出:
    1
      \
       2

示例 2:
输入:[3,0,4,None,2,None,None,1]
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

输出:[3,2,None,1]
      3
     /
   2
  /
 1
'''


class Node(object):
    def __init__(self,item):
        super(Node,self).__init__()
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.item)
    __repr__ = __str__

class Tree(object):
    def __init__(self):
        super(Tree,self).__init__()
        self.root = None
    def __str__(self):
        return str(self.root)
    # 创建二叉树
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

    # 深度遍历二叉树
    def wide_travel(self):
        des_list = []
        if self.root is not None:
            queue = []
            queue.append(self.root)
            while queue:
                temp = queue.pop(0)
                des_list.append(temp.item)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
        return des_list


    # 处理逻辑：不符合L=< 节点.item <=R 的节点剔除后，若有left或right，有left优先left上位，都没有补None
    # 修剪搜索的二叉树
    def modify_binary_tree(self,root,l,r):
        if root is None: # 根为None
            return root
        if root.item is not None and root.item < l:
            return self.modify_binary_tree(root.right,l,r)
        if root.item is not None and root.item > r:
            return self.modify_binary_tree(root.left,l,r)
        root.left = self.modify_binary_tree(root.left,l,r)
        root.right = self.modify_binary_tree(root.right,l,r)
        return root

if __name__ == '__main__':
    origin_list = [3,0,4,None,2,None,None,1]
    tree = Tree()
    [tree.add(item) for item in origin_list]
    des_list = tree.wide_travel()
    root =  tree.modify_binary_tree(tree.root,1,3)
    print(des_list)
