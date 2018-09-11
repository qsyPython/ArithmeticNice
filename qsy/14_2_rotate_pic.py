'''
    翻转图像：矩阵翻转
    给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

示例 1:

输入: [[1,1,0],[1,0,1],[0,0,0]]
输出: [[1,0,0],[0,1,0],[1,1,1]]
解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
示例 2:

输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
说明:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1

'''

# n行n列的矩阵,先执行水平翻转，后执行图片翻转


# 水平翻转
def level_rotate(origin_list):
    # 翻转list
    def revese_list(list, start, end):
        while start < end:
            temp = list[start]
            list[start] = list[end]
            list[end] = temp
            start += 1
            end -= 1
    for list in origin_list:
        revese_list(list,0,len(list)-1)
    return origin_list

# 翻转图片
def rotate_pic(origin_list):
    # 反转list值
    def exchange_value(list):
        for index,item in enumerate(list):
            if item == 0:
                list[index] = 1
            else:
                list[index] = 0
        return list

    level_rotate(origin_list)
    for list in origin_list:
        exchange_value(list)
    return origin_list

print(rotate_pic([[0,0,1],[0,1,1]]))
print(rotate_pic([[1,0,1],[1,1,1]]))
# 011,001


