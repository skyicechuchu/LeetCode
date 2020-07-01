"""
https://leetcode.com/problems/rotate-list/
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        The algorithm is quite straightforward :
        Find the old tail and connect it with the head old_tail.next = head to close the ring.
        Compute the length of the list n at the same time.
        Find the new tail, which is (n - k % n - 1)th node from the head and the new head, which is (n - k % n)th node.
        Break the ring new_tail.next = None and return new_head.
        """
        if not head: return None
        if not head.next: return head
        
        c = 1
        old_tail = head
        while old_tail.next:
            c += 1
            old_tail = old_tail.next
        old_tail.next = head
        
        new_tail = head
        for i in range(c - k % c - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        new_tail.next = None
        return new_head