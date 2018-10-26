'''
    单词替换：
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例 1:

输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"
注:

输入只包含小写字母。
1 <= 字典单词数 <=1000
1 <=  句中词语数 <= 1000
1 <= 词根长度 <= 100
1 <= 句中词语长度 <= 1000
'''
# string 包含子字符串的方式->
# 1、in方式：只要包含该字段就ok，不涉及到位置
# 2、find方式: 具体到某个index开始包含某字符串
# 3、index方式: 从字符起始的序号开始处理（如 0）

def word_replace(root_dict_list,sentence):
    sentence_list = sentence.split(' ')
    for index,item in enumerate(sentence_list):
        for root_word in root_dict_list:
            if root_word in item and item.index(root_word)==0:# 首字母开始判断
                sentence_list[index] = root_word
                break
    return ' '.join(sentence_list)
# print(word_replace(['cat', 'bat', 'rat','by'],'the cattle batcatlle was rattled by the battery'))
print(word_replace(["a","b","c"],"aadsfasf absbs bbab cadsfafs"))
