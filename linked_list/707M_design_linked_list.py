"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. 
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the next node. 
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list.
 After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. 
If index equals to the length of linked list, the node will be appended to the end of linked list. 
If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
"""


import unittest


class ListNodeSingle:
    def __init__(self, val):
        self.val = val
        self.next = None


class MySingleLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNodeSingle(0)
        self.size = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size: return None
        pre = self.head
        for _ in range(index + 1):
            pre = pre.next
        return pre.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        
        if index <= 0:
            index = 0
        
        self.size += 1
        pre = self.head
        for _ in range(index):
            pre = pre.next
        
        to_add = ListNodeSingle(val)
        to_add.next = pre.next
        pre.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size: return None
        self.size -= 1
        pre = self.head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next


class ListNodeDouble:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class MyDoubleLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head, self.tail = ListNodeDouble(0), ListNodeDouble(0)
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size: return -1
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.pre
        return curr.val



    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        l, r = self.head, self.head.next
        self.size += 1
        to_add = ListNodeDouble(val)
        to_add.pre = l
        to_add.next = r
        l.next = to_add
        r.pre = to_add

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        l, r = self.tail.pre, self.tail
        self.size += 1
        to_add = ListNodeDouble(val)
        to_add.pre = l
        to_add.next = r
        l.next = to_add
        r.pre = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index <= 0: index = 0
        if index > self.size: return

        if index < self.size - index:
            l = self.head
            for _ in range(index):
                l = l.next
            r = l.next
        else:
            r = self. tail
            for _ in range(index):
                r = r.pre
            l = r.pre

        self.size += 1
        to_add = ListNodeDouble(val)
        to_add.pre = l
        to_add.next = r
        l.next = to_add
        r.pre = to_add


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index <= 0: index = 0
        if index > self.size: return

        if index < self.size - index:
            l = self.head
            for _ in range(index):
                l = l.next
            r = l.next.next
        else:
            r = self. tail
            for _ in range(index):
                r = r.pre
            l = r.pre.pre

        self.size -= 1
        l.next = r
        r.prev = l

class TestCase(unittest.TestCase):

    def testcase1(self):
        linkedlist = MySingleLinkedList()
        linkedlist.addAtHead(1)
        linkedlist.addAtTail(3)
        linkedlist.addAtIndex(1, 2)
        self.assertEqual(linkedlist.get(1), 2)
        linkedlist.deleteAtIndex(1)
        self.assertEqual(linkedlist.get(1), 3)

    def testcase2(self):
        linkedlist = MyDoubleLinkedList()
        linkedlist.addAtHead(1)
        linkedlist.addAtTail(3)
        linkedlist.addAtIndex(1, 2)
        self.assertEqual(linkedlist.get(1), 2)
        linkedlist.deleteAtIndex(1)
        self.assertEqual(linkedlist.get(1), 3)
    

if __name__ == "__main__":
    unittest.main()