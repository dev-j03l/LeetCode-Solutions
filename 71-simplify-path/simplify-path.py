class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [p for p in path.split("/") if p]

        stack = []
        for part in parts:
            if part == "..":
                if not stack: continue
                stack.pop()
            elif part == ".":
                continue
            else:
                stack.append(part)
        
        if stack: stack.insert(0, "")
        
        return "/".join(stack) if stack else "/"