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

def lowest_common(x,y):
    des_list = []
    if x == 0 or y == 0:
        return 0
    if x < y:
        temp = x
        x = y
        y = temp
    temp_x = x
    temp_y = y
    while y:
        common = x % y
        x = y
        y = common
    return temp_x * temp_y/x

def selfDividingNumbers(left,right):
    num = []
    for index in range(left,right+1):
        s = str(index)
        for i in range(0,len(s)):
            if i == 0:
                temp = int(s[0])
            temp = lowest_common(int(s[i]),temp)
        if int(temp) == 0:
            continue
        if index % int(temp) == 0:
            num.append(index)
    return num

print(selfDividingNumbers(1,22))


