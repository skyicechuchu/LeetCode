"""
https://leetcode.com/problems/odd-even-linked-list/
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd = head # Both of them point at the first node of the target linked list
        even = head.next # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even # We have to keep where the even-node list starts
        
        while even and even.next: # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next
            even.next = even.next.next
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next
            even = even.next
        
        odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
        
        return head # We keep the start of the odd-node list in the first of our code