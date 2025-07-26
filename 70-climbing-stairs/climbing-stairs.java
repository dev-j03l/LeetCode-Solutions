class Solution {
    public int climbStairs(int n) {
        return climbStairs(n, new int[n+1]);
    }

    private int climbStairs(int n, int[] cache){
        if(n <= 2) return n;
        if(!(cache[n] == 0)) return cache[n];
        cache[n] = climbStairs(n-1, cache) + climbStairs(n-2, cache);
        return cache[n];
    }
}

