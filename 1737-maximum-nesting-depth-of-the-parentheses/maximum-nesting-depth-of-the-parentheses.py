class Solution:
    def maxDepth(self, s: str) -> int:
        max_len = 0
        stack = []
        opening = {"{", "[", "("}
        closing = {"}", "]", ")"}

        for ch in s:
            if ch in opening:
                stack.append(ch)
            elif ch in closing:
                stack.pop()

            max_len = max(max_len, len(stack))
        return max_len