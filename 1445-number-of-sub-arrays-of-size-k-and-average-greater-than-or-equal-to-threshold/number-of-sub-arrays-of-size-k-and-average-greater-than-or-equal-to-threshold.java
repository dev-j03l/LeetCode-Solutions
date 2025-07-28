class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int subArraySum = 0;
        int count = 0;
        int L = 0;
        for(int R = 0; R < arr.length; R++){
            subArraySum += arr[R];
            if(R - L + 1 == k){
                if(subArraySum/k >= threshold) count++;
                subArraySum -= arr[L];
                L++;
            }
        }
        return count;
    }
}