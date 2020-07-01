"""
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergetwo(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
    
    def mergetwo(self, l1, l2):
        sentinel = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if not l1:
            cur.next = l2
        else:
            cur.next = l1
        return sentinel.next
    
"""
Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.

We can merge two sorted linked list in O(n)O(n) time where nn is the total number of nodes in two lists.
Sum up the merge process and we can get: O\big(\sum_{i=1}^{log_{2}{k}}N \big)= O(N\log k)O(∑ 
i=1
log 
2
​	
 k
​	
 N)=O(Nlogk)
Space complexity : O(1)O(1)

We can merge two sorted linked lists in O(1)O(1) space.
"""