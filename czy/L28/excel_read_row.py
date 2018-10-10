# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:
#
# 输入: "A"
# 输出: 1
# 示例 2:
#
# 输入: "AB"
# 输出: 28
# 示例 3:
#
# 输入: "ZY"
# 输出: 701
#思路：相当于26进制转化成10进制，参考2进制转10进制。

def read_row_number(s):
    if (s is None) or len(s) == 0 :
        return 0

    value = 0
    sum = 0
    b = 1
    i = len(s) - 1
    while i >= 0:
        value = b*(ord(s[i]) - ord('A') + 1)
        sum += value
        b = b*26
        i -= 1
    return sum

if __name__ == '__main__':
   print(read_row_number("AB"))