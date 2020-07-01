"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
You are given a doubly linked list which in addition to the next and previous pointers,
 it could have a child pointer, which may or may not point to a separate doubly linked list. 
 These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, 
 as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
 You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects 
to the upper node of the previous level.
 The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
Accepted
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class SolutionDfsRec(object):

    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)

class SolutionStack(object):
    def flatten(self, head):
        if not head:
            return 
        stk=[head]
        prev=Node(0)
        while stk:
            root=stk.pop()
            root.prev=prev
            prev.next=root
            prev=root
            if root.next:
                stk.append(root.next)
            if root.child:
                stk.append(root.child)
                root.child=None
                
        head.prev=None
        return head


class Solution(object):
    def flatten(self, head):
        # Initialize the current reference and stack of saved next pointers
        curr, tempStack = head, []
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future reattachment
                    tempStack.append(curr.next)
                # Current <-> Current.child
                #   \-> None
                curr.next, curr.child.prev, curr.child = curr.child, curr, None
            if not curr.next and len(tempStack):
                # If the current node is a child without a next pointer
                temp = tempStack.pop()
                # Current <-> Temp
                temp.prev, curr.next = curr, temp
            curr = curr.next
        return head