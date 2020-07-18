"""
https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swappairs(head):
    """
    Inituation: iterative. 
    Time: O(N)
    Space: O(1)
    """
    dummy = ListNode(0)
    prev = dummy
    dummy.next = head
    
    while head and head.next:
        first_node = head
        second_node = head.next

        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev = first_node
        head = first_node.next

    return dummy.next

def swapparis_2(head):
    """
    Inituation: recursive
    Time: O(N)
    Space: O(N)
    """
    if not head or not head.next:
        return head

    first_node = head
    second_node = head.next

    first_node.next = swapparis_2(second_node.next)
    second_node.next = first_node
    return second_node
