class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        j = 0
        for i in range(min(len(word1), len(word2))):
            new_str = new_str + word1[i]
            new_str = new_str + word2[i]
            j = i+1
        
        if len(word1) > len(word2): new_str = new_str + word1[j:]
        if len(word2) > len(word1): new_str = new_str + word2[j:]

        return new_str
        