'''
    键盘行：
    给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
    QWERTYUIOP
    ASDFGHJKL
    ZXCVBNM

    示例1:
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
注意:

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

'''
first_list_str = 'QWERTYUIOP' # "QWERTYUIOPqwertyuiop";
second_list_str = 'ASDFGHJKL' # "ASDFGHJKLasdfghjkl";
third_list_str = 'ZXCVBNM' # "ZXCVBNMzxcvbnm";
def string_in_list_str(origin_str,char_list_str):
    for c in origin_str:
        if c not in char_list_str and chr(ord(c)-32) not in char_list_str:# 为大写和小写字母时的处理
            return False
    return True

def find_words(words_list):
    des_list = []
    for item in words_list:
        is_in_first_str = string_in_list_str(item,first_list_str)
        is_in_second_str = string_in_list_str(item, second_list_str)
        is_in_third_str = string_in_list_str(item, third_list_str)
        if is_in_first_str or is_in_second_str or is_in_third_str:
            des_list.append(item)
    return des_list

print(find_words(["Hello", "Alaska", "Daddddd", "Peace"]))