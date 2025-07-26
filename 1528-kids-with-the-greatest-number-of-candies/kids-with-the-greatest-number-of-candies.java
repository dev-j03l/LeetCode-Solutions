class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int greedyKid = 0;
        for(int n : candies) greedyKid = Math.max(greedyKid, n);
        List<Boolean> res = new ArrayList<>();
        for(int n : candies){
            if(n + extraCandies >= greedyKid) res.add(true);
            else res.add(false);
        }
        return res;
    }
}