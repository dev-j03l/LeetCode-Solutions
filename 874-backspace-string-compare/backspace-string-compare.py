class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []

        for char in s:
            if char == "#":
                if stack: stack.pop()
            else:
                stack.append(char)
        
        s = "".join(stack)
        stack.clear()
        for char in t:
            if char == "#":
                if stack: stack.pop()
            else:
                stack.append(char)
        
        t = "".join(stack)

        return s == t
