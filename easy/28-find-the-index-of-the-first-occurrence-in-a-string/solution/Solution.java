class Solution {
    public int strStr(String haystack, String needle) {
        for(int i = 0, j = needle.length(); j <= haystack.length(); j++,i++){
            if(haystack.substring(i,j).equals(needle)) return i;
        }
        return -1;
    }
}