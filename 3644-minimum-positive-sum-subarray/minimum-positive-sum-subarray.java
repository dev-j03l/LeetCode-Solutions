class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int minSum = Integer.MAX_VALUE;
        int n = nums.size();

        for (int size = l; size <= r; size++) {
            if (size > n) break;
            int windowSum = 0;

            for (int i = 0; i < size; i++) {
                windowSum += nums.get(i);
            }
            if (windowSum > 0) minSum = Math.min(minSum, windowSum);

            for (int i = size; i < n; i++) {
                windowSum += nums.get(i) - nums.get(i - size);
                if (windowSum > 0) minSum = Math.min(minSum, windowSum);
            }
        }

        return minSum == Integer.MAX_VALUE ? -1 : minSum;
    }
}
