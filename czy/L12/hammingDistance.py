# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。

#方法一
#使用异或和n&(n-1)技巧
# 对两个二进制数进行异或，得到的结果中某位为1，则对应的原来两个数中该位是不同的。
# 而使用n&(n-1)可以使得n的二进制数表示中最后一位1变成0。例如n=110, n-1=101, 则n&(n-1)=100。
# 综上，可以对两个数进行异或之后使用n&(n-1)技巧计算不同的位数。这种方法无需遍历二进制数中的所有位, 只比较不同的位。

# def hammingDistance(x = int,y = int):
#
#     if x >= 0 and y < 231:
#         z = x^y #将两个整数异或，保留不同位的1
#         count = 0
#         while z:  #将二进制最后一位变为0，直到整个数都变为0
#             z &= z - 1
#             count += 1
#         return count
#     return 0
#方法二
#暴力计算，将整数转换成二进制，相同位比较，不同则个数加1
def hammingDistance(x = int,y = int):
    if x >= 0 and y < 231:
        listX = list(bin(x)[2:])
        listY = list(bin(y)[2:])
        lenX = len(listX)
        lenY = len(listY)
        maxLen = max(lenX,lenY)
        if lenX > lenY:
            for i in range(lenY,lenX):
                listY.insert(0,"0")
        elif lenX < lenY:
            for i in range(lenX,lenY):
                listX.insert(0,"0")

        total = 0
        for i in range(maxLen):
            if listX[i] != listY[i]:
                total += 1
        return total


if __name__ == '__main__':
        print(hammingDistance(0,230))




