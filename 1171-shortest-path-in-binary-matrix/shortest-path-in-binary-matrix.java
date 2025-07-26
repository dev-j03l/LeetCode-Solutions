class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int ROWS = grid.length, COLS = grid.length;
        int[][] visit = new int[ROWS][COLS];
        Deque<int[]> q = new ArrayDeque<>();

        q.add(new int[2]); // {0, 0}
        visit[0][0] = 1;
        int length = 1;
        if(grid[0][0] == 1) return -1;
        while(! q.isEmpty()){
            int qLength = q.size();
            for(int i = 0; i < qLength; i++){
                int[] pair = q.poll();
                int r = pair[0], c = pair[1];
                if(r == ROWS-1 && c == COLS-1) return length;

                int[][] neighbours = {{r, c+1}, {r, c-1}, {r+1, c}, {r-1,c}, {r+1, c+1},
                {r+1, c-1}, {r-1, c+1}, {r-1, c-1}};

                for(int j = 0; j < 8; j++){
                    int newR = neighbours[j][0];
                    int newC = neighbours[j][1];

                    if(Math.min(newR, newC) < 0 || newR == ROWS || newC == COLS || 
                    visit[newR][newC] == 1 || grid[newR][newC] == 1) continue;

                    q.add(neighbours[j]);
                    visit[newR][newC] = 1;
                }
            }
            length++;
        }
        return length == 1? length : -1;
    }
}