# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None: #if the length is 1 return None
            return None
        
        slow = head
        fast = head
        
        while fast and fast.next and fast.next.next and fast.next.next.next:
            slow=slow.next
            fast=fast.next.next

        slow.next= slow.next.next #link middle-1 to middle+1
        
        return head

        return cHead
