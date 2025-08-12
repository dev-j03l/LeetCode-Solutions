class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find middle using slow & fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: If odd length, skip the middle node
        if fast:  # fast is not None → odd length
            slow = slow.next
        
        # Step 3: Reverse the second half
        second_half = self._reverse(slow)
        
        # Step 4: Compare the two halves
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
