'''
    数字的补数

给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。

示例 1:
输入: 5  二进制：101
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。

示例 2:
输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。

'''

# 数字转为二进制:返回list
def num_convert_binary_num(num):
    des_list = []
    while num:
        temp_num = num % 2
        des_list.insert(0,str(temp_num))
        num = num // 2
    return des_list

# 取补数：返回str
def complement(origin_list):
    des_list = []
    for index,item in enumerate(origin_list):
        if item == '1':
            des_list.insert(index,'0')
        else:
            des_list.insert(index, '1')
    return ''.join(des_list)

# 二进制转为数字
def binary_num_convert_num(binary_num_str):
    total_num = 0
    for index,item in enumerate(binary_num_str):
        total_num += int(item)*2**(len(binary_num_str)-1-index)
    return total_num

if __name__ == '__main__':
    origin_list = num_convert_binary_num(3)
    comple_str = complement(origin_list)
    des_num = binary_num_convert_num(comple_str)
print(des_num)



