# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#
#
# American keyboard
#
#
# 示例1:
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
# 注意:
#
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。

def searchWorld():
     array1 = [['Q','W','E','R','T','Y','U','I','O','P'],
              ['A','S','D','F','G','H','J','K','L'],
              ['Z','X','C','V','B','N','M']]
     array2 = ["Hello", "Alaska", "Dad", "Peace"]
     array3 = []
     for k in range(len(array1)) :

         for i in range(len(array2)):
             isExist = True
             str = array2[i]
             for j in range(len(str)):
                 char = str[j].upper()
                 if char in array1[k]:
                     isExist = True
                 else:
                     isExist = False
             if isExist:
                 array3.append(str)


     return array3


if __name__ == '__main__':

    print(searchWorld())





