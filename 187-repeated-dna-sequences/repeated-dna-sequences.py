class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = defaultdict(int)

        if len(s) < 10: return []

        L = 0
        for R in range(9, len(s)):
            sequences[s[L:R+1]] += 1
            L += 1

        res = []
        for x in sequences.items():
            if x[1] > 1: res.append(x[0])
        
        return res