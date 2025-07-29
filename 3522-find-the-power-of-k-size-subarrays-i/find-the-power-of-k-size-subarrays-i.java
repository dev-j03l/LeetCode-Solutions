class Solution {
    boolean isInAsc(int[] nums, int l, int r){
        for(int i = l; i < r; i++){
            if(nums[i] + 1 != nums[i+1]) return false;
        }
        return true;
    }
    public int[] resultsArray(int[] nums, int k) {
        if(nums.length ==  1) return nums;
        boolean isInAsc = true;
        int  l = 0, r = k -1;
        int arr[] = new int[nums.length - k + 1];
        while(r < nums.length){
            if(isInAsc(nums, l , r)) arr[l] = nums[r];
            else{
            arr[l] = -1;
            }
            l++;
            r++;
        }
        return arr;
    }
}