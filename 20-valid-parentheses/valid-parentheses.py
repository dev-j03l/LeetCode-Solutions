class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        stack = []
        for ch in s:
            if ch in pairs:
                if not stack: return False
                popped = stack.pop()
                if pairs[ch] != popped: return False
            else:
                stack.append(ch)
        
        return not stack