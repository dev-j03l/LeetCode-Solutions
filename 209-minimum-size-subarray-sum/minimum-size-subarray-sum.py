class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                length = min(length, R-L+1)
                curr_sum -= nums[L]
                L += 1
        
        return 0 if length == float('inf') else length