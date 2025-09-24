class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for s in strs:
            freq_count = [0] * 26
            for ch in s:
                freq_count[ord(ch) - ord('a')] += 1
            
            result[tuple(freq_count)].append(s)
        
        return list(result.values())