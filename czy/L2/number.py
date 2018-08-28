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

# 一 创建临时数组，切片保存实现数组反转
# def rotateArrayWithNode(array,k):
#         tempArray = [];
#         arrayLength = len(array);
#         relk = k%arrayLength;
#         tempArray.extend(array[0:arrayLength - relk])
#         for a in array[arrayLength:arrayLength - relk - 1:-1]:
#             tempArray.insert(0,a)
#         print(tempArray);

# # #二、 使用反转函数 reversed 排序函数 sorted 实现
# def rotateArrayWithNode(array,k):
#     arrayLength = len(array);
#     relk = k % arrayLength;
#     jointArray = list(reversed(array[arrayLength - relk:arrayLength])) + array[0:arrayLength - relk];
#    # jointArray = sorted(array[arrayLength - relk:arrayLength], key=None, reverse=True) + array[0:arrayLength - relk];
#     print(jointArray);


#三、 使用栈、队列
def rotateArrayWithNode(array,k):
    relk = k % len(array);
    for i in range(relk):
        node = array.pop();
        array.insert(0,node)
    print(array);


def main():
      array = [1,2,3,4,5,6];
      rotateArrayWithNode(array,2)

if __name__ == '__main__':
    main();