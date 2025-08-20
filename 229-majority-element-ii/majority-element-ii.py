class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n = n/3
        freq_count = defaultdict(int)
        res = set()
        for num in nums:
            freq_count[num] += 1
            if freq_count[num] > n: res.add(num)
        return list(res)
