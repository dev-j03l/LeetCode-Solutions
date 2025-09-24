class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letter_to_row = {}
        for l in "qwertyuiop":
            letter_to_row[l] = 1
        
        for l in "asdfghjkl":
            letter_to_row[l] = 2
        
        for l in "zxcvbnm":
            letter_to_row[l] = 3
        
        res = []
        for word in words:
            res.append(word)
            
            for i in range(1, len(word)):
                if letter_to_row[word[i].lower()] != letter_to_row[word[i-1].lower()]:
                    res.pop()
                    break
        
        return res


