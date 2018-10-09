# 编写一个程序，找到两个单链表相交的起始节点。
#
#
#
# 例如，下面的两个链表：
#
# A:          a1 → a2
# ↘
# c1 → c2 → c3
# ↗
# B:     b1 → b2 → b3
# 在节点
# c1
# 开始相交。
#
#
#
# 注意：
#
# 如果两个链表没有交点，返回
# null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足
# O(n)
# 时间复杂度，且仅用
# O(1)
# 内存。

# 思路是这样的（题目中假设没有环）： 
# 	1.分别遍历两个链表，如果尾节点不同则不相交，返回None，如果尾节点相同则求相交结点。 
# 	2.求相交结点的方法是，求出链表长度的差值，长链表的指针先想后移动lenA-lenB。然后两个链表一起往后走，若结点相同则第一个相交点。 
# 	3.求链表的长度，在遍历的时候就计算，并将每个结点放在字典中。 
# 	该题中不让修改链表结构。所以只考虑以上思路。还有另一种方法是： 
# 	先遍历第一个链表到他的尾部，然后将尾部的next指针指向第二个链表(尾部指针的next本来指向的是null)。这样两个链表就合成了一个链表，判断原来的两个链表是否相交也就转变成了判断新的链表是否有环的问题了：即判断单链表是否有环？ 
#
# ---------------------
class Node:
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)

class chainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
          item = None
          if isinstance(dataOrNode, Node):
              item = dataOrNode
          else:
              item = Node(dataOrNode)

          if not self.head:
              self.head = item
              self.length += 1

          else:
              node = self.head
              while node._next:
                  node = node._next
              node._next = item
              self.length += 1


def getIntersectionNode(headA = Node, headB = Node):
       p1 = headA
       p2 = headB
       while (p1.data != p2.data):
           p1 = headB if p1 == None else p1._next
           p2 = headA if p2 == None else p2._next
       return p1

def single_linked_list():
    a = [1,2,3,7,10]
    b = [9,11,3,7,10]

    chainTable1 = chainTable()

    for value in a:
        chainTable1.append(value)

    chainTable2 = chainTable()

    for value in b:
        chainTable2.append(value)

    p = getIntersectionNode(chainTable1.head,chainTable2.head)

    print(p)


if __name__ == '__main__':
    single_linked_list()
