# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        connected = False
        nums = set(nums)
        cur = head
        count = 0
        while cur:
            if cur.val in nums:
                if not connected:
                    count += 1
                    connected = True
            else:
                connected = False
            cur = cur.next
        return count