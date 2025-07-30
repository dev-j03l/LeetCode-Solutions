class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxAverage = Integer.MIN_VALUE;
        double rollingSum = 0;
        int left = 0;
        for(int right = 0; right < nums.length; right++){
            rollingSum += nums[right];
            if(right - left + 1 == k){
                maxAverage = Math.max(maxAverage, rollingSum/k);
                rollingSum -= nums[left];
                left++;
            }
        }

        return maxAverage;
    }
}