class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        counter = Counter(s)
        not_complacent = 0
        for key, val in counter.items():
            if val % 2 != 0: not_complacent += 1
                
        
        return True if not_complacent <= 1 else False