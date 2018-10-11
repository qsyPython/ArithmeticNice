# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
# 示例:
#
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。

def over_add_operate(num = int):
    if num > 9:
        num_str = str(num)
        sum = 0
        for i in range(len(num_str)):
            sum += int(num_str[i])
        if len(str(sum)) > 1:
           return over_add_operate(sum)
        else:
           return sum

    else:
        return num


if __name__ == '__main__':
   print(over_add_operate(38))