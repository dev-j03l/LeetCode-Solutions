class Solution:
    def reverseVowels(self, s: str) -> str:
        L = 0
        R = len(s) - 1
        s = list(s)
        vowels = "aeiouAEIOU"

        while L < R:
            while s[L] not in vowels and L< R:
                L += 1
            while s[R] not in vowels and L<R:
                R -= 1
            
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            L+= 1
            R -= 1
    
        return "".join(s)

