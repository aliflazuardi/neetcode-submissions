# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        l2 = slow.next
        slow.next = None

        #reverse l2
        prev = None

        while l2:
            nxt = l2.next
            l2.next = prev

            prev = l2
            l2 = nxt
        
        l1 = head
        l2 = prev
        curr = ListNode()

        while l1 and l2:
            curr.next = l1
            l1 = l1.next

            curr.next.next = l2
            l2 = l2.next
            
            curr = curr.next.next

        curr.next = l1 or l2