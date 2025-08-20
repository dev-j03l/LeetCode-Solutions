class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        a0 = []
        a1 = []
        for num in nums1:
            if num not in nums2:
                a0.append(num)
            
        for num in nums2:
            if num not in nums1:
                a1.append(num)

        return [a0, a1]
        