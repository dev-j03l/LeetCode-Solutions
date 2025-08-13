# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode()
        dummy.next = head
        cur = dummy.next
        prev = dummy

        while cur:
            if cur.val == val:
                tmp = cur.next
                prev.next = tmp
                cur = tmp
            else:
                prev = cur
                cur = cur.next

        return dummy.next
        