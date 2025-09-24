class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I" : 1,
            "V" : 5,
            "X" : 10, 
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        result = 0

        for i in range(len(s)):
            curr = mapping[s[i]]
            next_val = mapping[s[i+1]] if i+1 < len(s) else 0

            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result