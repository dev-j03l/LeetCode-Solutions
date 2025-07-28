class Solution {
    public int maxVowels(String s, int k) {
        int maxVowels = 0;
        int subStringVowels = 0;
        String vowels = "aeiou";
        int L = 0;

        for(int R = 0; R < s.length(); R++){
            if(vowels.indexOf(s.charAt(R)) != -1) subStringVowels++;
            if(R - L + 1 == k){
                maxVowels = Math.max(subStringVowels, maxVowels);
                if(vowels.indexOf(s.charAt(L)) != -1) subStringVowels--;
                L++;
            }
        }
        return maxVowels;
    }
}