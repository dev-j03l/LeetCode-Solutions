class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        rolling_total = 0
        num_greater = 0

        for R in range(len(arr)):
            rolling_total += arr[R]
            if R-L+1 > k:
                rolling_total -= arr[L]
                L += 1
            if R-L+1 == k and rolling_total/k >= threshold: num_greater += 1
        
        return num_greater
