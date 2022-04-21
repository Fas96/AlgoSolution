class Solution {
    public int prefixCount(String[] words, String pref) {
        int prefixCount=0;
        for(String word :words){
            if(word.length()>=pref.length() && word.substring(0,pref.length()).matches(pref)){
                prefixCount++;
            }
        }
        return prefixCount;
    }
}