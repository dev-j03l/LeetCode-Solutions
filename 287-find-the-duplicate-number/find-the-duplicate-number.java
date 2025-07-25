class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0;

        while(true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if(slow == fast) break;
        }

        int slow2 = 0;
        while(slow2 != slow){
            slow2 = nums[slow2];
            slow = nums[slow];
        }
        return slow;
    }
}