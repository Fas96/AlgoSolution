class Solution {
      public List<Integer> findSubstring(String s, String[] words) {
        HashMap<String, Integer> map = new HashMap<>();
        int len = words[0].length();
        int wordsLen = len * words.length;
        List<Integer> result = new LinkedList<>();
        for(String word: words) {
            map.put(word, map.getOrDefault(word, 0)+1);
        }
        for (int i = 0; i + wordsLen <= s.length(); i++) {
            String tmp = s.substring(i, i+wordsLen);
            if (containsWords(tmp, new HashMap<>(map), len)) {
                result.add(i);
            }
        }
        return result;
    }
    
    public boolean containsWords(String s, HashMap<String, Integer> map, int len) {
        boolean[] dp = new boolean[s.length()+1];
        Arrays.fill(dp, false);
        dp[0] = true;
        for(int i = len; i <= s.length(); i+=len) {
            String tmp = s.substring(i-len, i);
            if (dp[i-len] && map.containsKey(tmp) && map.get(tmp) > 0) {
                map.put(tmp, map.get(tmp)-1);
                dp[i] = true;
            }
        }
        return dp[s.length()];
    }
}