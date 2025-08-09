class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                index = stack.pop()[1]
                answer[index] = i - index
            stack.append([temp, i])
        return answer

                
        