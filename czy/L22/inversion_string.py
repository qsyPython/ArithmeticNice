# 编写一个函数，其作用是将输入的字符串反转过来。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "olleh"
# 示例 2:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: "amanaP :lanac a ,nalp a ,nam A"

def reverseString(s):

    if not s is None:
        i = 0
        length = len(s)
        array = list(s)
        while i < int(length / 2):
            tmp = array[i]
            array[i] = s[length - 1 - i]
            array[length - 1 - i] = tmp
            i += 1
        return ''.join(array)

    else:
        return None


if __name__ == '__main__':

    s = "hello"
    print(reverseString(s))