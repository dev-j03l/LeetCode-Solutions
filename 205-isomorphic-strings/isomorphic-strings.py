class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_indices = {}
        t_indices = {}
        for i, letter in enumerate(zip(s,t)):
            if letter[0] not in s_indices:
                s_indices[letter[0]] = [i]
            else:
                s_indices[letter[0]].append(i)

            if letter[1] not in t_indices:
                t_indices[letter[1]] = [i]
            else:
                t_indices[letter[1]].append(i)
 

        return list(t_indices.values()) == list(s_indices.values())