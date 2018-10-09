'''

相交链表：
编写一个程序，找到两个单链表相交的起始节点。
例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始相交。


注意：

如果2个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。



# 用途：2个链表相交，一旦程序释放了链表L1的所有节点，而L2的使用者并不知道，会造成麻烦
'''
# 思路1：首部链接，若成环，则有相交，若没有，则平行。
# 思路2：记录2个链表的长度；长度大的链表先移动，当剩余长度和长度短的链表长度相同，此后一起移动，判断后续节点是否相同
class Node(object): # 节点类
    def __init__(self,item):
        super(Node,self).__init__()
        self.item = item
        self.next = None
    def __str__(self):
        return str(self.item)

class Linked_list(object): # 链表类：链表表头和链表长度
    def __init__(self):
        super(Linked_list,self).__init__()
        self.head = None
        self.length = 0

    # 添加
    def add(self,item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.length += 1
        else:
            new_node = self.head
            while new_node.next:
                new_node = new_node.next
            new_node.next = node
            self.length += 1

    # 删除某位置的节点
    def delete(self,index):
        if self.length == 0:
            print('this chain table is empty.')
            return
        if index <0 or index>=self.length:
            print('error: out of index')
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node.next and j<index:
            prev = node
            node = node.next
            j += 1
        if j == index:
            prev.next = node.next
            self.length -= 1
    # 修改节点
    def update(self,index,item):
        if self.length == 0 or index< 0 or index>self.length:
            print('error: out of index')
            return
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1
        if j == index:
            node.item = item

    # 根据index查找item
    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1
        return node.data

    # 根据item查找index
    def getIndex(self, item):
        j = 0
        if self.length == 0:
            print('this chain table is empty')
            return
        node = self.head
        while node:
            if node.item == item:
                return j
            node = node.next
            j += 1

        if j == self.length:
            print('%s not found' % str(item))
            return
    # 删除整个链表
    def clear(self):
        self.head = None
        self.length = 0

def getIntersectionNode(head_a,head_b):
    if head_a is None or head_b is None:
        return None
    temp_a,temp_b = head_a,head_b
    len_a,len_b = temp_a.length,temp_b.length
    diff = len_a -len_b
    if diff > 0:









if __name__ == '__main__':
    list1 = ['a1','a2','c1','c2','c3']
    list2 = ['b1','b2','c1','c2','c3']
    linked_list1 = Linked_list()
    linked_list2 = Linked_list()
    [linked_list1.add(item) for item in list1]
    [linked_list2.add(item) for item in list2]
    print('')










