# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #current slow is at lower mid
        head2 = self._reverse(slow.next)
        max_sum = 0
        while head and head2:
            print(head.val, head2.val)
            max_sum = max(head.val + head2.val, max_sum)
            head = head.next
            head2 = head2.next
        
        return max_sum
            
    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev