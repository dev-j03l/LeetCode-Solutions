class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        L = 0
        num_good = 0
        window = set()

        for R in range(len(s)):
            while s[R] in window or R-L+1 > 3:
                window.remove(s[L])
                L += 1
            if R - L + 1 == 3: num_good += 1
            window.add(s[R])
        
        return num_good