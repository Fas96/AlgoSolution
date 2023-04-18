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
        int ffl=fl-minLen;
        int ssl=sl-minLen;
        if(ffl>-1){
            for (int j = i; j < fl; j++) {
                sb.append(word1.charAt(j));
                
            }
        }
        if(ssl>-1){
            for (int j = i; j < sl; j++) {
                sb.append(word2.charAt(j));

            }
        }


        return sb.toString();
    }
}