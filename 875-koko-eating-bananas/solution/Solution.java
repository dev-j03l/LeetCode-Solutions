class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = max(piles);
        int mid = left + (right-left)/2;

        while(left <= right){
            mid = left + (right-left)/2;
            if(isCorrect(piles, mid, h)){
                right = mid-1;
            } else{
                left = mid + 1;
            }
        }
        return left;
    }

    public boolean isCorrect(int[] piles, int k, int h){
        int sum = 0;
        for(int x: piles){
            sum += (int)Math.ceil((double)x/k);
        }
        return sum <= h;
    }

    public int max(int[] piles){
        int max = -1;
        for(int x: piles){
            if(x > max){
                max = x;
            }
        }
        return max;
    }
}
