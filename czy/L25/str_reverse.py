# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
#反转数组
def reverse_array(array,start,end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -=1
    return  array

#反转字符串中单词
def strReverse(str):
    tempArray = []
    array = str.split(' ')
    for index,value in enumerate(array):
        tempArray.append(''.join(reverse_array(list(value),0,len(value)-1)))
    return ' '.join(tempArray)

if __name__ == '__main__':
    print(strReverse("Let's take LeetCode contest"))





