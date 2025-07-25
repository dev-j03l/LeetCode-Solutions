class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        int[][] visit = new int[grid.length][grid[0].length];

        for(int m = 0; m < grid.length; m++){
            for(int n = 0; n < grid[0].length; n++){
                if(grid[m][n] == 1){
                    maxArea = Math.max(dfs(grid, m, n, visit), maxArea);
                }
            }
        }
        return maxArea;
    }

    private int dfs(int[][] grid, int r, int c, int[][] visit){
        int ROWS = grid.length, COLS = grid[0].length;
        if(Math.min(r,c) < 0 || r == ROWS || c == COLS || 
        grid[r][c] == 0 || visit[r][c] == 1) return 0;
        visit[r][c] = 1;
        int currArea = 1;
        currArea += dfs(grid, r+1, c, visit);
        currArea += dfs(grid, r-1, c, visit);
        currArea += dfs(grid, r, c+1, visit);
        currArea += dfs(grid, r, c-1, visit);
        grid[r][c] = 0;
        return currArea;
    }
}
