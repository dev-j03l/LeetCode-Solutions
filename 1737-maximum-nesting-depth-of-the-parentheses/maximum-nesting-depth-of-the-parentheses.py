class Solution:
    def maxDepth(self, s: str) -> int:
        max_len = 0
        count = 0

        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
            max_len = max(count, max_len)

        return max_len