'''
   按奇偶校验排序数组

给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

你可以返回满足此条件的任何数组作为答案。



示例：

输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。


提示：

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''

def sort_array(origin_list):
    for index,item in enumerate(origin_list[:]):
        if item%2 == 0:
            origin_list.pop(index) # remove只是删除list中靠近最前面的一项;故选择pop方式，定点清除！！！
            origin_list.insert(0,item)
    return origin_list
print(sort_array([1,3,4,4,5,6]))



