class Solution {
    public int maxSum(int[] nums) {
        int maxSum = 0;
        int maxElement = Integer.MIN_VALUE;
        HashSet<Integer> seen = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            if(nums[i] > 0 && !seen.contains(nums[i])) maxSum+= nums[i];
            maxElement = Math.max(nums[i], maxElement);
            seen.add(nums[i]); 
        }
        return maxSum == 0 ? maxElement:maxSum;
    }
}