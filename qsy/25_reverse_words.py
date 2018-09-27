'''
字符串反转
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''

def reverse_words(origin_str):
    origin_list = origin_str.split(' ')
    des_list = []
    for item in origin_list:
        # item = item[::-1] # 1、字符串截取反转
        order_item_list = [] # 2、转成list进行反转处理
        for c in item:
            order_item_list.append(c)
        order_item_list.reverse()
        item = ''.join(order_item_list)

        des_list.append(item)
    return ' '.join(des_list)

print(reverse_words("Let's take LeetCode contest"))