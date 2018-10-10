'''
自除数：
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：

输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
注意：

每个输入参数的边界满足 1 <= left <= right <= 10000。
'''

# 获取一个数各个位置上的数字,转为str后再强转为list
def get_loc_num(num):
    num_str = str(num)
    loc_list = list(num_str)
    return loc_list

# 判断1个数是否是自然数
def is_natural_number(item):
    temp = get_loc_num(item)
    for inner_item in temp:
        if int(inner_item) == 0 or item % int(inner_item) != 0:
            is_natural = False
            break
        else:
            is_natural = True
    return is_natural

def selfDividingNumbers(left, right):
    natural_list = []
    if left != right:
        for item in range(left, right+1):
            if is_natural_number(item):
                natural_list.append(item)
    else:
        if is_natural_number(left):
            natural_list.append(left)
    return natural_list

print(selfDividingNumbers(1,22))

