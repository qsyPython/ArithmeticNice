
# 在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
#
# 现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
#
# 你需要输出替换之后的句子。
#
# 示例 1:
#
# 输入: dict(词典) = ["cat", "bat", "rat"]
# sentence(句子) = "the cattle was rattled by the battery"
# 输出: "the cat was rat by the bat"
# 注:
#
# 输入只包含小写字母。
# 1 <= 字典单词数 <=1000
# 1 <=  句中词语数 <= 1000
# 1 <= 词根长度 <= 100
# 1 <= 句中词语长度 <= 1000

# 字典树
# 又称单词查找树，Trie树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。

# 它有3个基本性质：
# 根节点不包含字符，除根节点外每一个节点都只包含一个字符； 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串； 每个节点的所有子节点包含的字符都不相同。
class TrieNode:
    def __init__(self, x):
        self.val = x
        self.children = [None for _ in range(26)]
        self.isEnd = False

def insertStr(str, root):
        if str == None or str == "": return
        for ch in list(str):
            pos = ord(ch) - ord('a')
            if root.children[pos] == None:
                root.children[pos] = TrieNode(ch)
            else:
                pass
            root = root.children[pos]
        root.isEnd = True

def replaceWords( dict, sentence):

        root = TrieNode(None)
        for word in dict:
            insertStr(word, root)
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            res = ""
            node = root
            for j in range(len(sentence[i])):
                pos = ord(sentence[i][j]) - ord('a')
                if node.children[pos] != None:
                    res += node.children[pos].val
                    node = node.children[pos]
                else:
                    break
                if node.isEnd == True:
                    sentence[i] = res
                    break
        return " ".join(sentence)

if __name__ == '__main__':
    print(replaceWords(["cat", "bat", "rat"],"the cattle was rattled by the battery"))

