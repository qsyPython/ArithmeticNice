'''
子集：
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
# 0 : 1;
# 1: C len(nums)->1;
# 2: C len(nums)->2;
# n: C len(nums)->n;
# 转化为 ---> 组合怎么表示，
# 实现方法1：借用第3方库 itertools
# 实现方法2：手动处理，获取排列组合

import itertools
# def subset(nums):
#     subset_nums = []
#     for index in range(len(nums)):
#         for item in itertools.combinations(nums, index+1):
#             subset_nums.append(list(item))
#     empty_num = []
#     subset_nums.append(empty_num)
#     return subset_nums

# 双层循环和拷贝：res=[] res[:]  temp=[] temp[:]
def subset(nums):
    res = [[]]
    for num in nums:
        for temp in res[:]:
            x = temp[:]
            x.append(num)
            res.append(x)
    return res


print(subset([1,2,3,4,5]))