'''
     反转字符串
编写一个函数，其作用是将输入的字符串反转过来。

示例 1:

输入: "hello"
输出: "olleh"
示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
'''

def revert_string(s):
    # 方法1：使用字符串切片
    # result = s[::-1]

    # 方法2：list的reverse
    l = list(s)
    l.reverse()
    result = "".join(l)
    return result



print(revert_string('wojiushi,,,zhemshuaizemle'))