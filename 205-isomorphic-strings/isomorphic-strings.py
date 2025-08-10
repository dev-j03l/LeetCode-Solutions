class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_indices = {}
        for i, letter in enumerate(s):
            if letter not in s_indices:
                s_indices[letter] = [i]
            else:
                s_indices[letter].append(i)
        
        t_indices = {}
        for i, letter in enumerate(t):
            if letter not in t_indices:
                t_indices[letter] = [i]
            else:
                t_indices[letter].append(i)
                
        return list(t_indices.values()) == list(s_indices.values())