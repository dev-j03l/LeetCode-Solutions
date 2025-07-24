class Solution {
    public int maxSubArray(int[] nums) {
        // Brute-Force Solution O(N^2);
        // int maxSum = nums[0];

        // for(int i = 0; i < nums.length; i++){
        //     int curSum = 0;
        //     for(int j = i; j < nums.length; j++){
        //         curSum += nums[j];
        //         maxSum = Math.max(maxSum, curSum);
        //     }
        // }
        // return maxSum;

        // Kadane's Algorithm O(n)
        int maxSum = nums[0];
        int curSum = 0;

        for(int n: nums){
            curSum = Math.max(curSum , 0) + n;
            maxSum = Math.max(curSum, maxSum);
        }
        return maxSum;
    }
}