# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
#
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
#
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
#
# 示例 1:
#
# 输入: [[1,1,0],[1,0,1],[0,0,0]]
# 输出: [[1,0,0],[0,1,0],[1,1,1]]
# 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
# 示例 2:
#
# 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 说明:
#
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1
#将数组倒序（包括将其中的一段倒序，p为起始指针，length 需要反转的长度）
def invertedOrder(array,p,length):
    for i in range(int(length/2)):
        temp = array[i + p]
        array[i + p] = array[length + p - 1 -i]
        array[length + p - 1 -i] = temp
#水平反转
def horizontalFlip(binMatrix):
    if not binMatrix is None:
        for values in binMatrix:
            invertedOrder(values,0,len(values))
#取反
def invertValues(binMatrix):
    if not binMatrix is None:
        for values in binMatrix:
            for i in range(len(values)):
                if values[i] == 0:
                    values[i] = 1
                elif values[i] == 1:
                    values[i] = 0

if __name__ == '__main__':
    arr_bin_num = [[1,1,0],[1,0,1],[0,0,0]]
    print ('原矩阵:')
    print (arr_bin_num)
    horizontalFlip(arr_bin_num)
    print ('水平翻转后矩阵:')
    print (arr_bin_num)
    invertValues(arr_bin_num)
    print ('反转图像:')
    print (arr_bin_num)



