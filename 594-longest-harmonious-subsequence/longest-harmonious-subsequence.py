class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_count = defaultdict(int)

        for num in nums:
            freq_count[num] += 1
        
        maxlength = 0
        for num in freq_count:
            if num + 1 in freq_count:
                currLength = freq_count[num] + freq_count[num+1]
                maxlength = max(currLength, maxlength)

        return maxlength 