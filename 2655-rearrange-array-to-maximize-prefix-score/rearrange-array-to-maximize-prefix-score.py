class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        runningtotal = 0
        score = 0
        for num in nums:
            runningtotal += num
            if runningtotal > 0: score += 1
        
        return score
        