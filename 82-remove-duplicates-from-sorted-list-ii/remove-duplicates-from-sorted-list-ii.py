# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        freq_count = defaultdict(int)

        while current:
            freq_count[current.val] += 1
            current = current.next
        
        prev = dummy =  ListNode(0, head)
        current = head

        while current:
            if freq_count[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next