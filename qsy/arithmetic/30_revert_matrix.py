'''

转置矩阵：
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
[1,2,3]
[4,5,6]
[7,8,9]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
[1,2,3]
[4,5,6]

提示：

1 <= A.length <= 1000
1 <= A[0].length <= 1000
'''

# 行数和列数交换：for range 2次遍历
def revert_matrix(two_dimensional_array):
    des_arry = []
    row = len(two_dimensional_array) #获取总行数：决定每个新1维list的len
    column = len(two_dimensional_array[0]) #获取总列数：决定一维list的个数
    for i in range(column):
        one_dimensional_array = []
        for j in range(row):
            one_dimensional_array.append(two_dimensional_array[j][i])
        des_arry.append(one_dimensional_array)
    return des_arry
print(revert_matrix([[1,2,3],[4,5,6],[7,8,9]]))