class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 0

        nums.sort()
        mx = 0
        count = 0
        mn = float('inf')
        ans = float('inf')
        l = 0
        for r in range(len(nums)):
            mx = max(mx, nums[r])
            mn = min(mn, nums[r])
            count += 1
            while count > k:
                count -= 1
                l += 1
                mn = nums[l]
            
            if count == k:
                 ans = min(ans, mx-mn)
        
        return ans