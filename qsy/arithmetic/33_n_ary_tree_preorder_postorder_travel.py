'''
    N叉树的前序和后序遍历:

给定一个 N 叉树，返回其节点值的前序和后序遍历。

例如，给定一个 3叉树 :
          1

   3      2        4

 5   6

返回其前序遍历: [1,3,5,6,2,4]。
返回其后序遍历: [5,6,3,2,4,1]。

'''

class Node(object):
    def __init__(self,val,node_list):
        super(Node,self).__init__()
        self.val = val
        self.node_list = node_list
    def __str__(self):
        return str(self.val)

class N_ary_tree(object):
    def __init__(self):
        super(N_ary_tree,self).__init__()
        self.root = None

    # 添加节点
    def add(self,item):
        pass

    # 前序遍历
    def preorder(self):
        pass

    # 后续遍历
    def postorder(self):
        pass


