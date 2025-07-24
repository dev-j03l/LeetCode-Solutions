class Solution {
    public int search(int[] nums, int target) {
        // First let us set the left and right pointers
        int left = 0;
        int right = nums.length-1;

        while(left <= right){
            // calculate mid
            int mid = (left + right)/2;

            if(target > nums[mid]){
                left = mid + 1;
            } 
            else if (target < nums[mid]){
                right = mid - 1;
            } else {
                // target == mid
                return mid;
            }
        }

        return -1;
    }
}
