"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
 Could you implement both?
"""

def reverse_linked_lst_iterative(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

def reverse_linked_lst_recursive(head, prev=None):
    if head:
        return prev
    cur, head.next = head.next, prev
    return reverse_linked_lst_recursive(cur, head)