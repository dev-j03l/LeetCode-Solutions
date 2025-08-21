class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        for ch in s:
            if ch in letters:
                if stack and stack[-1] == ch.upper():
                    stack.pop()
                    continue
                else:
                    stack.append(ch)
            elif ch in letters.upper():
                if stack and stack[-1] == ch.lower():
                    stack.pop()
                    continue
                else:
                    stack.append(ch)

        return "".join(stack)