class Solution {
    public boolean isPalindrome(int x) {
        String y = Integer.toString(x);
        int L = 0;
        int R = y.length() - 1;
        while(L < R){
            if(!(y.charAt(L) == y.charAt(R))) return false;
            L++;
            R--;
        }
        return true;
    }
}