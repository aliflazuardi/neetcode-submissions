# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        pointer = curr

        for i in range(n):
            pointer = pointer.next

        while pointer:
            pointer = pointer.next

            prev = curr
            curr = curr.next

        if prev == None:
            return head.next
        
        prev.next = curr.next
        
        return head