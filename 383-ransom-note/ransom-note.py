class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for letter in magazine:
            letters[letter] += 1
        
        for letter in ransomNote:
            letters[letter] -= 1
        
        for val in letters.values():
            if val < 0:
                return False
        
        return True
        