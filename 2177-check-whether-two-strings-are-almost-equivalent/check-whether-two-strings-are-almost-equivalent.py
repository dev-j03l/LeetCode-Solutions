class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = [0] * 26
        w2 = [0] * 26

        for n in word1:
            w1[ord(n) - ord('a')] += 1
        
        for n in word2:
            w2[ord(n) - ord('a')] += 1
        
        for l1, l2 in zip(w1, w2):
            if abs(l1 - l2) > 3: return False
        
        return True