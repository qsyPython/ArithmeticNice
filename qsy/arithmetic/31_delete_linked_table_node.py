'''
    删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

    4 -> 5 -> 1 -> 9
示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
'''

# 节点
class Node(object):
    def __init__(self,val):
        super(Node,self).__init__()
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

#链表: head 和 length
class Linked_tab(object):
    def __init__(self):
        super(Linked_tab,self).__init__()
        self.head = None
        self.length = 0

    # 添加节点
    def add(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.length +=1
        else: #获取链表中最后1个节点
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = node
            self.length += 1

    #  删除节点:val 左侧链表和右侧链表分别获取
    def delete_node_from_val(self,val):
        if self.length >0:
            temp_right_node = self.head
            if temp_right_node.val == val:
                if self.length == 1:
                    self.head = None
                    self.length -= 1
                else:
                    self.head = self.head.next
                    self.length -= 1
            else:
                temp_left_node = Node(temp_right_node.val)
                while temp_right_node.next:
                    if temp_right_node.next.val == val:
                        if (temp_right_node.next).next:
                            temp_right_node = (temp_right_node.next).next
                        else:
                            temp_right_node = None
                        break
                    else:
                        temp_left = temp_left_node
                        while temp_left.next:
                            temp_left = temp_left.next
                        temp_left.next = Node(temp_right_node.next.val)
                        temp_right_node = temp_right_node.next
                temp_last_left = temp_left_node
                while temp_last_left.next:
                   temp_last_left = temp_last_left.next
                temp_last_left.next = temp_right_node
                self.length -= 1
                self.head = temp_left_node
        return self.head

    ##  删除节点:index
    def delete_node_from_index(self,index):
        if self.length > 0:
            if index >= 0 and index < self.length: #index在节点范围内
                if self.length == 1:
                    self.head = None
                    self.length -= 1
                else:
                    if index == 0:
                        self.head = self.head.next
                        self.length -= 1
                    else:
                        left_temp = Node(self.head.val)
                        right_temp = self.head
                        for i in range(self.length):
                            if i == index:
                                right_temp = right_temp.next
                                break
                            else:
                                temp_left_middle = left_temp
                                while temp_left_middle.next:
                                    temp_left_middle = temp_left_middle.next

                                # 获取index对应item
                                temp_head_node = self.head
                                j = 0
                                while temp_head_node.next and j<i:
                                    temp_head_node = temp_head_node.next
                                    j += 1
                                if i !=0:
                                    temp_left_middle.next = Node(temp_head_node.val)
                                right_temp = right_temp.next

                        temp_last_left = left_temp
                        while temp_last_left.next:
                            temp_last_left = temp_last_left.next
                        temp_last_left.next = right_temp
                        self.length -= 1
                        self.head = left_temp
            else:
                print("所删节点超出范围")
        return self.head

    # 根据index获取item
    def get_item(self,index):
        if self.length <= 0 or index :
            print('不再可选范围内')
        else:
            temp_node = self.head



if __name__ == '__main__':
    node_list = [1,3,3,5,6]
    linked_tab = Linked_tab()
    [linked_tab.add(item) for item in node_list]
    linked_tab.delete_node_from_val(1)
    linked_tab.delete_node_from_index(2)
    print('删除了一个节点')


