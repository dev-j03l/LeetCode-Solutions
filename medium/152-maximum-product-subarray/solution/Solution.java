class Solution {
    public int maxProduct(int[] nums) {
        // Bruteforce solution
        // int maxProduct = nums[0];
        
        // for(int i = 0; i < nums.length; i++){
        //     int currProduct = 1;
        //     for(int j = i; j < nums.length; j++){
        //         currProduct *= nums[j];
        //         maxProduct = Math.max(currProduct, maxProduct);
        //     }
        // }
        // return maxProduct;

        int maxProduct = nums[0], minProduct = nums[0], result = nums[0];

        for(int i = 1; i < nums.length; i++){
            int n = nums[i];
            if(n < 0){
                int temp = maxProduct;
                maxProduct = minProduct;
                minProduct = temp;
            }

            minProduct = Math.min(n, minProduct * n);
            maxProduct = Math.max(n, maxProduct * n);
            result  = Math.max(result, maxProduct);
        }
        return result;
    }
}