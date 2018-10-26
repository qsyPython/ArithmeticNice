'''
1、题目：两数之和

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
# 空间复杂度 O（1）、时间复杂度O(n2)
def twoSum( nums, target):
    rtype = []
    for i,value_i in enumerate(nums):
        for j,value_j in enumerate(nums):
#            所有符合的位置
#            if j>i and value_i + value_j == target:
#            满足同1元素只被使用1次时的条件
            if (j>i and value_i + value_j == target) and (i not in rtype and j not in rtype):
                rtype.append(i)
                rtype.append(j)
    rtype = list(set(rtype))
    return rtype


# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         map.put(nums[i], i);
#     }
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement) && map.get(complement) != i) {
#             return new int[] { i, map.get(complement) };
#         }
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }
# 时间复杂度：
# O(n)，我们只遍历了包含有n 个元素的列表2次。在表中进行的每次查找只花费 O(1) 的时间。
#
# 空间复杂度：O(n)， 所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 n 个元素

# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement)) {
#             return new int[] { map.get(complement), i };
#         }
#         map.put(nums[i], i);
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }
# 时间复杂度：
# O(n)，我们只遍历了包含有n 个元素的列表一次。在表中进行的每次查找只花费 O(1) 的时间。
#
# 空间复杂度：O(n)， 所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 n 个元素


print(twoSum([1,3,4,6,4,1],5))
