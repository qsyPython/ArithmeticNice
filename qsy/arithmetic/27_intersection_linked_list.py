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
#
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
        return node.item

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

# 2表相交
def get_intersection_node(head_a,head_b,head_a_length,head_b_length):
    if head_a is None or head_b is None:
        return None
    long_a,short_b = head_a,head_b
    len_a, len_b = head_a_length,head_b_length

    diff = len_a -len_b

    if len_a < len_b:
        diff = -diff
        long_a = head_b
        short_b = head_a

    for i in range(diff):
        long_a = long_a.next
    while long_a and short_b and long_a != short_b:
        long_a = long_a.next
        short_b = short_b.next
    return long_a

if __name__ == '__main__':
    list1 = ['a1','a2']
    list2 = ['b1','b2']
    common_list = ['c1','c2','c3']
    linked_list1 = Linked_list()
    linked_list2 = Linked_list()
    linked_list_common = Linked_list() # 创建公共的链表，拼接到其他2个链表后

    [linked_list1.add(item) for item in list1]
    [linked_list2.add(item) for item in list2]
    [linked_list_common.add(item) for item in common_list]

    # linked_list1.head.next = linked_list_common.head
    # linked_list2.head.next = linked_list_common.head

    # 注意：必须获取链表中最后1个节点，才能拼接新的； 同时处理链表的length
    temp1 = linked_list1.head
    while temp1.next:
        temp1 = temp1.next
    temp1.next = linked_list_common.head
    linked_list1.length += linked_list_common.length

    temp2 = linked_list2.head
    while temp2.next:
        temp2 = temp2.next
    temp2.next = linked_list_common.head
    linked_list2.length += linked_list_common.length

    result_head = get_intersection_node(linked_list1.head,linked_list2.head,linked_list1.length,linked_list2.length)
    print(result_head)








