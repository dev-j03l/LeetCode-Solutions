class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                curr = stack.pop()
                next_greater[curr] = num
            stack.append(num)
        
        return [next_greater.get(n, -1) for n in nums1]

        