# 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
#
# 行数 m 应当等于给定二叉树的高度。
# 列数 n 应当总是奇数。
# 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。
# 根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。
# 你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。
# 即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。
# 然而，如果两个子树都为空则不需要为它们留出任何空间。
# 每个未使用的空间应包含一个空的字符串""。
# 使用相同的规则输出子树。
# 示例 1:
#
# 输入:
#      1
#     /
#    2
# 输出:
# [["", "1", ""],
#  ["2", "", ""]]
# 示例 2:
#
# 输入:
#      1
#     / \
#    2   3
#     \
#      4
# 输出:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# 示例 3:
#
# 输入:
#       1
#      / \
#     2   5
#    /
#   3
#  /
# 4
# 输出:
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 注意: 二叉树的高度在范围 [1, 10] 中。

class Node():
    def __init__(self, data=None):
        self._data = data;
        self._left = None;
        self._right = None;

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self, node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self, node):
        self._right = node

    def get_right(self):
        return self._right

def printTreeRecur(root = Node,collection = list, m = int, pos = int, deepth = int):
    if not root:
        return;
    row = collection[deepth - 1]
    row[pos] = root.get_data();
    deepth  += 1
    step =pow(2,m-deepth)
    printTreeRecur(root.get_left(),collection,m,pos - step,deepth)
    printTreeRecur(root.get_right(),collection,m,pos + step,deepth)

def printTree(root = Node):
    m = depth(root);
    n = pow(2, m) - 1;
    collection = []
    for i in range(m):
        row = [''] * n
        collection.append(row)
    printTreeRecur(root, collection, m, int(n/2), 1)
    print(collection)


def depth(root = Node):
    if not root:
        return 0;
    if (not root.get_left()) and (not root.get_right()):
        return 1;
    return max(depth(root.get_left()), depth(root.get_right())) + 1;

if __name__ == '__main__':
    # 实例化根节点
    root_node = Node('a')
    #root_node.set_data('a')
    # 实例化左子节点
    left_node = Node('b')
    # 实例化右子节点
    right_node = Node('c')
    # 给根节点的左指针赋值，使其指向左子节点
    root_node.set_left(left_node)
    # 给根节点的右指针赋值，使其指向右子节点
    root_node.set_right(right_node)

    printTree(root_node)



