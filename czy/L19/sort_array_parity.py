# 给定一个非负整数数组
# A，返回一个由
# A
# 的所有偶数元素组成的数组，后面跟
# A
# 的所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
#
#
# 示例：
#
# 输入：[3, 1, 2, 4]
# 输出：[2, 4, 3, 1]
# 输出[4, 2, 3, 1]，[2, 4, 1, 3]
# 和[4, 2, 1, 3]
# 也会被接受。
#
#
# 提示：
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

def sortArrayByParity(array):
    length = len(array)
    result = [None]*length
    left = 0 #左边索引
    right = length - 1#右边索引
    i = 0
    while i < length:
        item = array[i]
        if item%2 == 0:
            result[left] = item
            left += 1
        else:
            result[right] = item
            right -= 1
        i += 1
    return result

if __name__ == '__main__':

    print(sortArrayByParity([3, 1, 2, 4]))



