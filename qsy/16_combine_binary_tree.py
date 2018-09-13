'''
   合并二叉树
   给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: [1,3,2,5]                  [2,1,3,null,4,null,7]
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出: [3,4,5,5,4,None,7]
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''

# 实现逻辑1：转为list后，对list进行求和合并处理
# 实现逻辑2：直接操作2个tree，得到新tree后，再深度遍历
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

    def add(self,item):
        # 添加节点
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
        # 深度遍历
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

# 合并二叉树逻辑：对左右分支做None判断处理；
def combine_binary(root1,root2):
    if root1 is None and root2 is None:
        return  None
    elif root1 is None:
        return root2
    elif root2 is None:
        return root1
    else:
        if root1.item is not None and root2.item is not None:
            root1.item +=root2.item
            root1.left = combine_binary(root1.left, root2.left)
            root1.right = combine_binary(root1.right, root2.right)
            return root1
        elif root1.item is not None and root2.item is None:
            root1.left = combine_binary(root1.left, root2.left)
            root1.right = combine_binary(root1.right, root2.right)
            return root1
        elif root1.item is None and root2.item is not None:
            root2.left = combine_binary(root1.left, root2.left)
            root2.right = combine_binary(root1.right, root2.right)
            return root2


# 补齐2个list的位数: 在last位数添加
def polishing_list(x_list, y_list):
    if len(x_list) == len(y_list):
        return
    if len(x_list) > len(y_list):
        for i in range(len(y_list), len(x_list)):
            y_list.append(None)
    if len(x_list) < len(y_list):
        for i in range(len(x_list), len(y_list)):
            x_list.append(None)

# 计算2list的和
def sum_list(x_list,y_list):
    result_list = []
    for i in range(len(origin_list1)):
        if origin_list1[i] is None or origin_list2[i] is None:
            if origin_list1[i] is None and origin_list2[i] is None:
                result_list.append(None)
            else:
                if origin_list1[i] is not None:
                    result_list.append(origin_list1[i])
                else:
                    result_list.append(origin_list2[i])
        else:
            result_list.append(origin_list1[i] + origin_list2[i])
    return result_list

if __name__ == '__main__':
    origin_list1 = [1,3,2,5]
    origin_list2 = [2,1,3,None,4,None,7]
    # 方法1
    # polishing_list(origin_list1,origin_list2)
    # result_list = sum_list(origin_list1,origin_list2)
    # print(result_list)
    # 方法2
    tree1 = Tree()
    tree2 = Tree()
    [tree1.add(item) for item in origin_list1]
    [tree2.add(item) for item in origin_list2]
    res_root = combine_binary(tree1.root,tree2.root)
    print(res_root)
# [3,4,5,5,4,none,7]







