class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double rollingSum = 0;
        double maxAverage = Integer.MIN_VALUE;
        int L = 0;
        for(int R = 0; R < nums.length; R++){
            rollingSum += nums[R];
            if(R-L+1 == k){
                maxAverage = Math.max(maxAverage, rollingSum/k);
                rollingSum -= nums[L];
                L++;
            }
        }   
        return maxAverage;
    }
}