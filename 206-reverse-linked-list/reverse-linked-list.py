# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head

        follower = head
        current = head.next
        follower.next = None
        while current:
            tmp = current.next
            current.next = follower
            follower = current
            current = tmp
        
        return follower
        