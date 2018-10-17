'''
    N叉树的最大深度:
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :
        1

  3       2      4

5   6


我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。

'''

# n叉树的节点: value 和 包含所有子树叉的list
class Node(object):
    def __init__(self,val,list):
        super(Node,self).__init__()
        self.val = val
        self.list = list

    def __str__(self):
        return str(self.val)

class N_ary_tree(object):
    def __init__(self):
        super(N_ary_tree,self).__init__()
        self.root = None

    # 添加节点
    def add(self,n,item):
        node = Node(item,[])
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                temp = queue.pop(0)
                if len(temp.list) < n:
                    temp.list.append(node)
                    break
                else:
                     for item in temp.list:
                         if item.val is not None and len(item.list)<n:
                             queue.append(item)
                             break

    # 深度遍历
    # def wide_travel(self):
    #     if self.root is not None:
    #
    #     # return  self.root

    # 获取最大深度
    def max_deepth(self,root,n):
        if root and len(root.list)>0:
            for item in root.list:
                return max(self.max_deepth(root.left), self.max_deepth(root.right)) + 1
        else:
            return 0


if __name__ == '__main__':
    origin_list = [1,3,5,6,7,8,9,None,10]
    n = 3 #n的叉数
    n_tree = N_ary_tree()
    [n_tree.add(n,item) for item in origin_list]
    max_deepth = n_tree.max_deepth(n_tree.root,n)
    print('我就是看看而已:%s'%(max_deepth))
