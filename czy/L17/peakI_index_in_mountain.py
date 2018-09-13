# 我们把符合下列属性的数组
# A
# 称作山脉：
#
# A.length >= 3
# 存在
# 0 < i < A.length - 1
# 使得A[0] < A[1] < ...
# A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1]
# 给定一个确定为山脉的数组，返回任何满足
# A[0] < A[1] < ...
# A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1]
# 的
# i
# 的值。
#
#
#
# 示例
# 1：
#
# 输入：[0, 1, 0]
# 输出：1
# 示例
# 2：
#
# 输入：[0, 2, 1, 0]
# 输出：1
#
# 提示：
#
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10 ^ 6
# A
# 是如上定义的山脉

def peakIndexInMountainArray(array):
    if not array is None:
        result = 0
        i = 0
        while i < len(array):
            if array[i] > array[i+1]:
                result = i
                break
            i += 1
        return result
    return None

if __name__ == '__main__':
    mountainArray = [1,2,3,5,8,3,2,0]
    print(peakIndexInMountainArray(mountainArray))



