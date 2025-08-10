class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_count = defaultdict(int)

        for num in arr:
            freq_count[num] += 1

        return len(set(freq_count.values())) == len(freq_count.values())
