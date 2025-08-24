class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_map = {"W": 0, "B" : 0}

        L = 0
        min_w = float("inf")
        for R in range(len(blocks)):
            count_map[blocks[R]] += 1
            while R-L+1 > k:
                count_map[blocks[L]] -= 1
                L += 1
            
            if R-L+1 == k:
                min_w = min(count_map["W"], min_w)
            
        return min_w