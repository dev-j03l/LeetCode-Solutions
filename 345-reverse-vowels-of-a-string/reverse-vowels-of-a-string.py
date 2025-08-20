class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        L, R = 0, len(s) - 1
        vowels = set("aeiouAEIOU")

        while L < R:
            while L < R and s[L] not in vowels:
                L += 1
            while L < R and s[R] not in vowels:
                R -= 1
            if L < R:
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1

        return "".join(s)
