class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        for c in count:
            if count[c] == 1:
                return s.index(c)
        
        return -1
            
