class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1
        
        for letter in t:
            letters[letter] -= 1
            if letters[letter] < 0:
                return letter
        return -1
        