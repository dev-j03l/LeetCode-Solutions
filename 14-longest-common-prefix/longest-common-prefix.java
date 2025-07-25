class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        int l1 = 0;
        int l2 = 0;
        String word1 = strs[0];
        String word2 = strs[strs.length-1];
        StringBuilder sb = new StringBuilder();
        // if(word1.equals("") || word2.equals("")) return "";
        while(l1 < word1.length() && l2 < word2.length() && (word1.charAt(l1) == word2.charAt(l2))){
            sb.append(word1.charAt(l1));
            l1++; l2++;
        }
        return sb.toString();
    }
}