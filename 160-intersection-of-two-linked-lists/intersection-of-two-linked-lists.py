# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_nodes = set()

        curr1 = headA
        curr2 = headB

        while curr1 or curr2:
            if curr1:
                if curr1 in seen_nodes:
                    return curr1
                seen_nodes.add(curr1)
                curr1 = curr1.next
            
            if curr2:
                if curr2 in seen_nodes:
                    return curr2
                seen_nodes.add(curr2)
                curr2 = curr2.next
        
        return None
                
        