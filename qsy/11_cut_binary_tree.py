'''
    作业：二叉树剪枝
    给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

    返回移除了所有不包含 1 的子树的原二叉树。

( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

示例1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1]

解释:
只有红色节点满足条件“所有不包含 1 的子树”。
右图为返回的答案。


示例2:
输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]



示例3:
输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]


说明:

给定的二叉树最多有 100 个节点。
每个节点的值只会为 0 或 1 。
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
        ''' 添加节点 '''
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
                   # 新增异常判断
                   if temp.left.item is not None:
                    queue.append(temp.left)
                   if temp.right.item is not None:
                    queue.append(temp.right)

    def wide_travel(self):
        ''' 深度遍历-广序遍历:从上到下,从左到右，利用队列 '''
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

    # 二叉树分支切掉: 后续遍历
    def cut_tree(self,root):
        if root is not None:
            root.left = self.cut_tree(root.left)
            root.right = self.cut_tree(root.right)
            # 判断当前节点是否要删除, 如果左右子树都是返回NULL并且当前节点的值为0, 就表明以当前节点为根节点的树里面的值全部为0,所以应该删除此节点,反之不用删除
            if root.left is None and root.right is None and root.item == 0:
                return None
        return root

if __name__ == '__main__':
    origin_list = [1,0,1,0,0,0,1]
    tree = Tree()
    for item in origin_list:
        tree.add(item)
    tree.cut_tree(tree.root)
    new_list = tree.wide_travel()
    print(new_list)














