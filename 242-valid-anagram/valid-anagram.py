class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) sorting #approach
        letters = defaultdict(int)
        for x in s:
            letters[x] += 1
        
        for x in t:
            letters[x] -= 1
        
        for x in letters.values():
            if x != 0:
                return False
        
        return True