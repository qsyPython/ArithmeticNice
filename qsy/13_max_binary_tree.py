'''
    最大二叉树
    给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

Example 1:

输入: [3,2,1,6,0,5]
输入: 返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
注意:

给定的数组的大小在 [1, 1000] 之间。
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
                    if temp.left.item is not None:
                        queue.append(temp.left)
                    if temp.right.item is not None:
                        queue.append(temp.right)

    def wide_trave(self):
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


# 获取最大元素，其左侧添到左二叉树，右侧添到右二叉树
    def max_add(self,nums):
        if len(nums) <= 0:
            return None
        else:
            max_value = max(nums)
            max_index = nums.index(max_value)
            left_nums,right_nums = [],[]
            for index,item in enumerate(nums):
                if index < max_index:
                    left_nums.append(nums[index])
                elif index > max_index:
                    right_nums.append(nums[index])
            node = Node(max_value)
            node.left = self.max_add(left_nums)
            node.right = self.max_add(right_nums)
            return node

if __name__ == '__main__':
    # origin_list = [1,3,8,None,None,None,None,None,None,None,4,19]
    # origin_list = [1,3,8,None,None,None,5]
    origin_list = [1,3,8,9,2,0]
    # origin_list = [None]
    # origin_list = []
    tree = Tree()
    tree.root = tree.max_add(origin_list)
    resut = tree.wide_trave()
    print(resut)

