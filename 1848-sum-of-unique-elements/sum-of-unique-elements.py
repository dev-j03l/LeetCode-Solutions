class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for x in nums:
            seen[x] += 1
        
        count = 0
        for x in nums:
            if seen[x] == 1:
                count += x
        return count