class Solution {
    public int orangesRotting(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        boolean[][] visit = new boolean[ROWS][COLS];

        Deque<int[]> q = new ArrayDeque<>();
        for(int i = 0; i < ROWS; i++){
            for(int j = 0; j < COLS; j++){
                if(grid[i][j] == 2) {
                    q.add(new int[]{i,j});
                    visit[i][j] = true;
                }
            }
        }
        int minutes = 0;
        while(!q.isEmpty()){
            boolean rotted = false;
            int qLength = q.size();
            for(int i = 0; i < qLength; i++){
                int[] pair = q.poll();
                int r = pair[0], c = pair[1];
                
                int[][] neighbours = {{r, c+1}, {r, c-1}, {r+1, c}, {r-1,c}};
                for(int j =0; j < 4; j++){
                    int newR = neighbours[j][0];
                    int newC = neighbours[j][1];

                    if(Math.min(newR, newC) < 0 || newR == ROWS || newC == COLS 
                    || visit[newR][newC] || grid[newR][newC] == 0) continue;

                    q.add(neighbours[j]);
                    visit[newR][newC] = true;
                    grid[newR][newC] = 2;
                    rotted = true;
                }
            }
            if(rotted) minutes++;
        }
        for (int[] row : grid) {
            for (int cell : row) {
                if (cell == 1) return -1;
            }
        }
        return minutes;
    }
}
