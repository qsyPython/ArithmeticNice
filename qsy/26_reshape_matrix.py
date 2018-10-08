'''
    重塑矩阵：
    在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

输入:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
输出:
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
示例 2:

输入:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
输出:
[[1,2],
 [3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
注意：

给定矩阵的宽和高范围在 [1, 100]。
给定的 r 和 c 都是正数。
'''

'''
 params：
     nums:二维数组
     r：行数
     c：列数
'''
def reshape_matrix(nums,r,c):
    total_length = 0
    one_dimensional_nums = []
    for item in nums:
        total_length +=len(item)
        for inner_item in item:
            one_dimensional_nums.append(inner_item)
    if r*c != total_length:
        return nums
    des_nums = []
    for i in range(r):# 获取新二维数组对应的行数，从第0行开始
        one_dimensional_des = one_dimensional_nums[i*c:(i+1)*c]
        des_nums.append(one_dimensional_des)
    return des_nums

print(reshape_matrix([[1,3,6],[15,26,37]],6,1))




