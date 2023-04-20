class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
         List<Integer> resultIndices = new ArrayList<Integer>();
        Map<String,Integer> wordFreqMap=new HashMap<>();
        for (String word : words) wordFreqMap.merge(word,1,Integer::sum);
        int wordLen=words[0].length();
        int wordsCount=words.length;
        for (int i = 0; i <= s.length()-wordLen*wordsCount; i++) {
            Map<String,Integer> seenMap=new HashMap<>();
            for (int j = 0; j < wordsCount; j++) {
                int nextWordIndex=i+j*wordLen;
                String nextWord=s.substring(nextWordIndex,nextWordIndex+wordLen);
                if(!wordFreqMap.containsKey(nextWord))break;
                seenMap.merge(nextWord,1,Integer::sum);
                if(seenMap.get(nextWord)>wordFreqMap.get(nextWord))break;
                if(j+1==wordsCount)resultIndices.add(i);
            }
        }
        return resultIndices;
    }
}