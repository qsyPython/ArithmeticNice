'''
    汉明距离:
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

5
    1
    0
    1

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置
'''

# 获取int对应的二进制
def get_binary_list(x,res_list = None):
    if res_list is None:
        res_list = []
    temp = x % 2  # 获取余数
    res_list.insert(0,temp)
    x = x // 2  # 获取商
    if x != 0:
        get_binary_list(x,res_list)
    return res_list

# 补齐2个list的位数
def polishing_list(x_list, y_list):
    if len(x_list) > len(y_list):
        for i in range(len(y_list), len(x_list)):
            y_list.insert(0, 0)
    if len(y_list) > len(x_list):
        for i in range(len(x_list), len(y_list)):
            x_list.insert(0, 0)

def hamming_distance(x,y):
    num = 0
    x_list = get_binary_list(x)
    y_list = get_binary_list(y)
    polishing_list(x_list,y_list)
    for i in range(len(x_list)):
        if x_list[i] != y_list[i]:
            num += 1
    return num

print(hamming_distance(2,5))
