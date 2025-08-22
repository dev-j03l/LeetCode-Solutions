class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0] * len(prices)
        stack = []

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                curr = stack.pop()
                answer[curr] = prices[curr] - p
            
            answer[i] = p
            stack.append(i)

        return answer