class Solution {
    public int numSimilarGroups(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str : strs) map.put(str, null);
        
        int ans = 0;
        for (String str : strs) {
            if (map.get(str) == null) {
                ans++;
                dfs(str, map);
            }
        }
        return ans;

    }

    private void dfs(String str, Map<String, List<String>> map) {
        if (map.get(str) != null) {
            return;
        }
        map.put(str, new ArrayList<>());
        for (String key : map.keySet()) {
            if (isSimilar(str, key)) {
                dfs(key, map);
            }
        }
    }

    private boolean isSimilar(String str, String key) {
           int diff = 0;
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) != key.charAt(i)) {
                    diff++;
                }
                if (diff > 2) {
                    return false;
                }
            }
            return true;
    }
}