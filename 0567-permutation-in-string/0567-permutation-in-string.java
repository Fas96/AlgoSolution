class Solution {
    public boolean checkInclusion(String s1, String s2) {
          int n = s1.length();
        int m = s2.length();
        Map<Character,Integer> s1Map = new HashMap<>();
        Map<Character,Integer> s2Map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            s1Map.merge(s1.charAt(i), 1, Integer::sum);
        }
       
        for (int i = 0; i <= m-n; i++) {
            String sub = s2.substring(i, i+n);
            for (int j = 0; j < n; j++) {
                s2Map.merge(sub.charAt(j), 1, Integer::sum);
            }
            if(s1Map.equals(s2Map)) return true;
            s2Map.clear();
        }
        return false;
    }
}