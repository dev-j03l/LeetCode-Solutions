class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for character in s:
            if character == "(" or character == "[" or character == "{":
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                if character == ")" and stack.pop() != "(":
                    return False
                elif character == "]" and stack.pop() != "[":
                    return False
                elif character == "}" and stack.pop() != "{":
                    return False
        return len(stack) == 0