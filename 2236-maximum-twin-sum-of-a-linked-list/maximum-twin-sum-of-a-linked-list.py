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
        
        head2 = slow.next
        slow.next = None
        prev = None
        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp
        head2 = prev
        
        max_sum = 0
        while head and head2:
            max_sum = max(head.val + head2.val, max_sum)
            head = head.next
            head2 = head2.next
        
        return max_sum