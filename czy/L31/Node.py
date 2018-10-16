# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#
# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:
#
#     4 -> 5 -> 1 -> 9
# 示例 1:
#
# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:
#
# 输入: head = [4,5,1,9], node = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
# 说明:
#
# 链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
# 不要从你的函数中返回任何结果。

class Node:
    def __init__(self,value,p = None):
        self.val = value
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            return

        elif key <0  or key > self.getlength():
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():

            return

        elif key <0  or key > self.getlength():

            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):

        p =  self.head
        length = 0
        while p is not None:
            length+=1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print('target is not exist!')

    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p
    #通过节点值
    def deleteNode(self, node = Node):
       if node is not None:
           tempN = self.head
           while tempN:
               if tempN.val == node.val:
                   tempN.val = tempN.next.val
                   tempN.next = tempN.next.next
               tempN = tempN.next

    # 通过下表删除
    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            return

        if index ==0:
            q = Node(0,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next is not None and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():

            return

        p = self.head
        i = 0
        while p.next is not None and (not p.val ==value):
            p = p.next
            i+=1

        if p.val == value:
            return i
        else:
            return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    l = LinkList()
    l.initlist(array)
  #  l.deleteNode(Node(2))

    index = l.index(2)
    l.delete(index)

    print(l.getlength())
