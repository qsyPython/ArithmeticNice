'''

转置矩阵：
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]


提示：

1 <= A.length <= 1000
1 <= A[0].length <= 1000
'''

def revert_matrix(two_dimensional_array):
    des_arry = []
    for index,item in enumerate(two_dimensional_array):
        one_dimensional_array = []
        for inner_index,inner_item in enumerate(item):
            one_dimensional_array.append(item)
        des_arry.append(one_dimensional_array)



print(revert_matrix([[1,3,5,7],[2,4,6,8]]))