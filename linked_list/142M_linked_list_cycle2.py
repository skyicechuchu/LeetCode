"""
https://leetcode.com/problems/linked-list-cycle-ii/
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""

def linked_cycle_hash(head):
    """
    Hash table to save visited node.
    Time: O(n)
    Space: O(n)
    """
    visited = set()
    node = head
    while node:
        if node in visited:
            return node
        else:
            visited.add(node)
            node = node.next
    return None

def linked_cycle_floyd(head):
    def getinterset(head):
        fast, slow = head
        while fast and fast.next:
            fast = fast.next.next
            if fast == slow:
                return slow
    
    interset = getinterset(head)
    if interset is None: return None
    p1, p2 = head, interset
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
    