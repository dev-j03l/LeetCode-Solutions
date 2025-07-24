class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for(int x: nums){
            if(seen.contains(x)) return x;
            seen.add(x);
        }
        return -1;
    }
}