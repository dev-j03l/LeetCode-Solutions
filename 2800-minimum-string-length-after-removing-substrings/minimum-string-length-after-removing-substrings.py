class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        match = {
            "B" : "A",
            "D" : "C"
        }

        for c in s:
            if stack and match.get(c) == stack[-1]: stack.pop() 
            else: stack.append(c)
        
        return len(stack)