class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int left = 0;
        int rollingSum = 0;
        int count = 0;

        for(int right = 0; right < arr.length; right++){
            rollingSum += arr[right];
            if(right-left+1 == k){
                if(rollingSum/k >= threshold) count++;
                rollingSum -= arr[left];
                left++;
            }
        }
        return count;
    }
}