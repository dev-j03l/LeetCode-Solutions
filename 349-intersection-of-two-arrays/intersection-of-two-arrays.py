class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        joint = defaultdict(int)
        for n in nums1:
            joint[n] =1
        res = []
        for n in nums2:
            if joint[n] == 1:
                res.append(n)
        return res