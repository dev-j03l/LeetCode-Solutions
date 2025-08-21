class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1+v2)
            elif ch == "*":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 * v2)
            elif ch == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif ch == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2/v1))
            else:
                stack.append(int(ch))
        
        return stack[-1]