# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
    res = [[]]
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            l = len(res)
        for j in range(len(res) - l, len(res)):
          res.append(res[j] + [nums[i]])
    return res

if __name__ == '__main__':
    print(subsets([1,2,2,2]))

