'''
对称二叉树

给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3,4,null,null,5] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
  /      \
  4       5
说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''
# 节点
class Node(object):
    def __init__(self,item):
        super(Node,self).__init__()
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.item)
# 树
class Tree(object):
    def __init__(self):
        super(Tree,self).__init__()
        self.root = None
    def add_node(self,item):
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
                else: # 都不为空,将左节点和右节点放入队列，等待新1轮的迭代; 新增异常nul时list的判断处理
                    if temp.left.item is not '':
                        queue.append(temp.left)
                    if temp.right.item is not '':
                        queue.append(temp.right)

# 处理root
def is_symmetric(root):
    if root is None:
        return True
    return isSymmetric(root.left, root.right)

def isSymmetric(root_left,root_right):
    if root_left is None and root_right is None:
        return True
    if root_left is None or root_right is None or root_left.item != root_right.item:
        return False
    return isSymmetric(root_left.left,root_right.right) and isSymmetric(root_left.right,root_right.left)

if __name__ == '__main__':# python中 None就是null,这个空对象；以''代表list中有 空节点
    origin_list = [1,2,2,3,3,'']
    tree = Tree()
    for item in origin_list:
        tree.add_node(item)
    origin_root = tree.root
    print(is_symmetric(origin_root))

