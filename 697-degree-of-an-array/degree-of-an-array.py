class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_count = Counter(nums)
        degree = max(freq_count.values())
        start_end = {}
        for i, item in enumerate(nums):
            if freq_count[item] == degree:
                if item not in start_end:
                    start_end[item] = [i, i]
                else:
                    start_end[item][1] = i
        
        min_sub = float('inf')
        for j in start_end.values():
            min_sub = min(j[1] - j[0], min_sub)
        
        return min_sub + 1
