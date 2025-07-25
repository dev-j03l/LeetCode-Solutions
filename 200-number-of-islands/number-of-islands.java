class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        int[][] visit = new int[grid.length][grid[0].length];
        for(int m = 0; m < grid.length; m++){
            for(int n = 0; n < grid[0].length; n++){
                if(grid[m][n] == '1'){
                    dfs(grid, m, n, visit);
                    count++;
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int r, int c, int[][] visit){
        int ROWS = grid.length, COLS = grid[0].length;
        if((Math.min(r,c) < 0) || r == ROWS || c == COLS || grid[r][c] == '0' || visit[r][c] == 1){
            return;
        }
        visit[r][c] = 1;
        dfs(grid, r+1, c, visit);
        dfs(grid, r-1, c, visit);
        dfs(grid, r, c+1, visit);
        dfs(grid, r, c-1, visit);
        grid[r][c] = '0';
    }
}
