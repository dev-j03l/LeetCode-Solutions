# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        left -= 1
        right -= 1

        while left <= right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
            left += 1
            right -= 1

        cur = head
        index = 0
        while cur:
            cur.val = arr[index]
            index += 1
            cur = cur.next
        return head