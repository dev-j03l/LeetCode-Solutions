class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length * 2];


        for(int i =0; i < nums.length; i++){
            ans[i] = nums[i];
        }

        for(int i = nums.length; i < nums.length*2; i++){
            ans[i] = nums[i-nums.length];
        }

        return ans;
    }
}