class Solution {
    public boolean isPalindrome(String s) {

        int j = s.length() - 1;
        int i = 0;
        s = s.toLowerCase();

        while(i <= j){
            while(i < j && !Character.isLetterOrDigit(s.charAt(j))){
                j--;
            }
            while(i < j && !Character.isLetterOrDigit(s.charAt(i))){
                i++;
            }
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
}
 