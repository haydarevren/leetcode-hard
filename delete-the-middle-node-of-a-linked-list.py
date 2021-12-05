# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count of nodes
        def lenList(head):
            count = 0
            while (head != None):
                head = head.next
                count += 1
            return count
        
        cHead = head
  
        # Find the count of nodes
        count = lenList(head)
        if count<=1: return None

        # Find the middle node
        mid = count // 2

        # Delete the middle node
        while (mid > 1):
            mid -= 1
            head = head.next

        # Delete the middle node
        head.next = head.next.next

        return cHead
