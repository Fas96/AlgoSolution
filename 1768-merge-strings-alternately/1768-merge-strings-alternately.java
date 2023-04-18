class Solution {
    public String mergeAlternately(String word1, String word2) {
        int fl=word1.length();
        int sl=word2.length();
        int minLen=Math.min(sl,fl);
        StringBuilder sb= new StringBuilder();
        int i=0;
        while (i<minLen){
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
            i++;
        }
        sb.append(word1.substring(minLen));
        sb.append(word2.substring(minLen));


        return sb.toString();
    }
}