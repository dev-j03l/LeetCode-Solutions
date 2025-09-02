class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        
        score = 0
        for i in range(len(prefix_sum)):
            if prefix_sum[i] > 0:
                score += 1
        
        return score
        