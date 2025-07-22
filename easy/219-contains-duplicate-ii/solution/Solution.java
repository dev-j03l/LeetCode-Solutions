import java.util.*;
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // Bruteforce:
        // for(int L = 0; L < nums.length; L++){
        //     for(int R = L+1; R < Math.min(nums.length, L+k+1); R++){
        //         if(nums[L] == nums[R]) return true;
        //     }
        // }
        // return false;

        int L = 0;
        HashSet<Integer> window = new HashSet<>();
        
        for(int R = 0; R < nums.length; R++){
            if( (R-L+1) > k + 1){
                window.remove(nums[L]);
                L++;
            }
            if(window.contains(nums[R])) return true;
            window.add(nums[R]);
        }
        return false;
    }
}