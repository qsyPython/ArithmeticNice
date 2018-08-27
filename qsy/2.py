'''
    2、题目：旋转数组
'''
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。
# 空间复杂度O(1)：为常量。即不随被处理数据量n的大小而改变！
# 原地算法:一种使用小的，空固定数量的额外之间来转换资料的算法。

# 1+2、逐个换位平移：新位置的数据会错位。每次移位之后，原数据有人接收才ok

# 普及：
# 时间复杂度是一个函数，它定量描述了该算法的运行时间!
# O(1)：无论算法def的输入n是多大，都不会影响到算法的运行时间，t是常量
# O(n)：随着输入的n变化，运行时间成比例增加！
# 空间复杂度：一个算法def在运行过程中临时占用存储空间大小的量度。
# 递归算法就要有O(n)：每次返回都要存储返回信息！
# O(1): 不随被处理数据量n的大小而改变时,算法def在运行过程中临时占用存储空间大小为常量
# O(n): for循环list的n、递归都是内部再次执行func

# (i+k)%n等于新i的思路，不过这次是每次调换一个元素，后一个元素的调换基于上一个的位置,O(1)
def rotate_nums(originList,location):
    remainder = location % len(originList)
    if remainder!=0:
        i = 0
            new_value = originList[i]
            start = 0
            index = 0
            while index < len(originList):
                index += 1
                i = (i + remainder)%len(originList)
                ord_value = originList[i]
                originList[i] = new_value
                if i == start:
                    start +=1
                    i +=1
                    new_value = originList[i]
                else:
                    new_value = ord_value
    return originList


print(rotate_nums([23,5,8,19,20],2))


# 第i个数该有的位置应该是 -> 在i+k这个位置上
# 第i个数该有的位置应该是 ->局部一次对折后位置为n-k-i ->整个对折 n-（n-k-i） ->  i+k
# 2、数组对折反转：先反转前n-k,再反转后k个元素，最后将整个数组反
# def rotate_nums(originList,location):
#     reminder = location%(len(originList))
#     reverse_num(originList,0,len(originList)-1-reminder)
#     reverse_num(originList,len(originList)-reminder,len(originList)-1)
#     reverse_num(originList,0,len(originList)-1)
#     return originList
#
# def reverse_num(originList, start, end): #翻转
#     while start < end:
#         tmp = originList[start]
#         originList[start] = originList[end]
#         originList[end] = tmp
#         start += 1
#         end -= 1

# print(rotate_nums([23,5,8,19,20],2))
# 3.借用1个新数组: i 和 i+k%len(list) 位置对应，由于遍历次数随数据源变化，所以是O(n)
# def rotateNums(originList,location):
#     remainder = location%len(originList)
#     if remainder == 0:
#         return originList
#     else:
#         new_nums = list(range(len(originList)))
#         for i,item in enumerate(originList):
#                 new_nums[(i+remainder)%len(originList)] = item
#         return new_nums
# print(rotateNums([23,5,8,19,19],1))




