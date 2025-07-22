class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int L = 0;
        int count = 0;
        double rollingTotal = 0;

        for(int R = 0; R < arr.length; R++){
            rollingTotal += arr[R]; 
            if((R-L+1) >= k){
                if(rollingTotal/k >= threshold) count++;
                rollingTotal -= arr[L];
                L++;
            }
        }
        return count;
    }
}