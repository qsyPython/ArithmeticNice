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

# 获取Cn m，条件：n>=m,且n不为0。如C4 1 = 4/1 = 6
def deal_factorial(n,m):
    if m == 0:
        return 1
    else:
        numerator = 1
        denominator = 1
        for index in range(n-m,n):
            numerator *= index+1
        for index in range(m):
            denominator *=index+1
        return numerator//denominator

# def get_total_nums(nums,single_list_count,total_list_num):
#     total_list = []
#     total_nums_list = single_list_count #single_list_count 代表list中元素数目
#     for index in range(total_list_num): #index 代表第几个list
#         single_list = []
#         for item in nums:
#             if item not in single_list:
#                 single_list.append(item)
#                 total_nums_list -= 1
#                 if total_nums_list == 0:
#                     break
#         total_list.append(single_list)
#     return total_list
# print(get_total_nums([1,2,3,4],1,4))

def subset(nums):
    subset_nums = []
    for index in range(len(nums)):
        single_list_count = index+1
        total_count = deal_factorial(len(nums),single_list_count)
        while total_count:
            subset = []
            for item in range(single_list_count):
                subset.append(nums[total_count - 1 - item])
            subset_nums.append(subset)
            total_count -=1
    empty_num = []
    subset_nums.append(empty_num)
    return subset_nums

print(subset([1,2,3,4]))
[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]