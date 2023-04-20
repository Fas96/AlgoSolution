class Solution {
    public int characterReplacement(String str, int k) {
         int windowStart=0;
        int maxLen=0;
        int maxRepeatLetterCount=0;
        Map<Character,Integer> charFrequencyMap=new HashMap<>();
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
            char rightChar = str.charAt(windowEnd);
            charFrequencyMap.merge(rightChar,1,Integer::sum);
            maxRepeatLetterCount=Math.max(maxRepeatLetterCount,charFrequencyMap.get(rightChar));
            if(windowEnd-windowStart+1-maxRepeatLetterCount>k){
                char leftChar = str.charAt(windowStart);
                charFrequencyMap.merge(leftChar,-1,Integer::sum);
                windowStart++;
            }
            maxLen=Math.max(maxLen,windowEnd-windowStart+1);
        }
        return maxLen;
    }
}