class Solution {
    public int maxArea(int[] heights) {
        // Formula for calculating the water:
        // Min(heights[L], height[R]) * (R - L).
        int L = 0;
        int R = heights.length - 1;
        int maxWater = 0;
        
        while(L < R){
            int currWater = (Math.min(heights[L], heights[R])) * (R - L);
            maxWater = Math.max(maxWater, currWater);
            if(heights[L] < heights[R]) L++;
            else R--;
        }
        return maxWater;
    }
}