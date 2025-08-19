# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Reverse the LL
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        head = prev

        max_right = -1
        dummy = ListNode(0, head)
        cur = dummy.next
        prev = dummy
        while cur:
            if cur.val < max_right:
                prev.next = cur.next
            else:
                max_right = cur.val
                prev = prev.next
            cur = cur.next
        
        prev = None
        head = dummy.next
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
