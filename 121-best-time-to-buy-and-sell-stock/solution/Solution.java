class Solution {
    public int maxProfit(int[] prices) {
        // Naive solution
        // int max = 0;
        // for(int i = 0; i < prices.length; i++){
        //     for(int j = i; j < prices.length; j++){
        //         if(prices[j] - prices[i] > max) max = prices[j] - prices[i];
        //     }
        // }
        // return max;

        int min = Integer.MAX_VALUE;
        int overall = 0;
        int profitToday = 0;

        for(int i = 0; i < prices.length; i++){
            if(prices[i] < min) min = prices[i];
            profitToday = prices[i] - min;
            if(overall < profitToday) overall = profitToday;
        }
        return overall;
    }
}