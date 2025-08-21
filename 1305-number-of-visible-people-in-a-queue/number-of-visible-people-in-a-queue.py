class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        result = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                curr = stack.pop()
                result[curr] += 1
            if len(stack) > 0:
                result[stack[-1]] += 1
            stack.append(i)
        return result