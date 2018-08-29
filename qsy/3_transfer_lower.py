'''
题目3：转换成小写字母
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

示例 1：
输入: "Hello"
输出: "hello"

示例 2：
输入: "here"
输出: "here"

示例 3：
输入: "LOVELY"
输出: "lovely"
'''
#  方法1：直接都转了； 方法2：遍历，遇到大写char，替换对应位置为小写;  方法3：使用python的chr()和ord()
def ToLowerCase(str):
    # str = str.lower()
    # return str

    for i,item in enumerate(str):
        if item.isupper():
            str = str.replace(item,item.lower(),i)
            # str = str.replace(item,chr(ord(item)+32),i) # 小写ASCLL码 比 大写ASCLL码大32
    return str
print(ToLowerCase('UUUi9998888TTT'))