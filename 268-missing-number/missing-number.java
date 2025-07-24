class Solution {
    public int missingNumber(int[] nums) {
        int totalSum = 0, numSum = 0;
        for(int i = 0; i <= nums.length; i++){
            totalSum += i;
            if(i < nums.length) numSum += nums[i];
        }

        return totalSum-numSum;
    }
}
