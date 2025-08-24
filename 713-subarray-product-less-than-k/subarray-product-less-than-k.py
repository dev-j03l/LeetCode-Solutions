class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        L = 0
        count = 0
        curr_product = 1

        for R in range(len(nums)):
            curr_product *= nums[R]
            while curr_product >= k:
                curr_product = int(curr_product/nums[L])
                L += 1
            count += R-L+1
        
        return count