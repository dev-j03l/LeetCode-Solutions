class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_counter = Counter(tuple(row) for row in grid)

        ans = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            ans += row_counter[col]
        return ans