# 今天的算法题：N叉树的前序遍历
# 给定一个
# N
# 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个
# 3
# 叉树:
#
# 返回其前序遍历: [1, 3, 5, 6, 2, 4]。

class Node(object):
    def __init__(self, val, children = None):
        self.val = val
        self.children = children

def preorder(root):
    if not root:
        return [];
    if not root.children:
        return [root.val];
    result = [root.val];
    for child in root.children:
        result += preorder(child);
    return result;


if __name__ == '__main__':

    node15 = Node(5)
    node26 = Node(6)
    node1 = Node(3)
    node1.children = [node15, node26]
    node2 = Node(2)
    node3 = Node(4)
    head = Node(1)
    head.children = [node1,node2,node3]
    print(preorder(head))