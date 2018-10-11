'''
位数相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
'''

# 并将list中的每个元素处理为int类型
def get_number_digit(num):
    num_str = str(num)
    num_list = list(num_str)
    num_list = [int(item) for item in num_list]
    return num_list

def digit_add(num):
    num_list = get_number_digit(num)
    total_sum = sum(num_list)
    while total_sum >=10:
        num_list = get_number_digit(total_sum)
        total_sum = sum(num_list)
    return total_sum

print(digit_add(110))