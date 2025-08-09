class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []
        for element in reversed(nums2):
            while stack and stack[-1] <= element:
                stack.pop()
            nextGreater[element] = -1 if not stack else stack[-1]
            stack.append(element)
        
        return [nextGreater[n] for n in nums1]

        