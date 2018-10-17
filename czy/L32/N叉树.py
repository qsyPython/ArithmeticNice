# 给定一个
# N
# 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个
# 3
# 叉树:
#
# 我们应返回其最大深度，3。
#
# 说明:
#
# 树的深度不会超过
# 1000。
# 树的节点总不会超过
# 5000。


class Node(object):
    def __init__(self, val, children = None):
        self.val = val
        self.children = children

def maxDepth(root):
     if not root:
            return 0
     if not root.children:
            return 1
     return 1 + max(maxDepth(child) for child in root.children)



if __name__ == '__main__':

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    head = Node(1)
    head.children = [node1,node2,node3]

    print(maxDepth(head))



