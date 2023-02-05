class Solution {
    public List<Integer> findAnagrams(String s, String p) {
         int n = s.length();
        int m = p.length();

        int[] pMap = new int[26];
        int[] sMap = new int[26];
//           Map<Character,Integer> sMap = new HashMap<>();
//           Map<Character,Integer> pMap = new HashMap<>();

        for (Character c : p.toCharArray()) {
            pMap[c - 'a']++;
//            pMap.merge(c, 1, Integer::sum);
        }

        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i <= n - m; i++) {
             // String sub = s.substring(i, i+n);
            for (int j = 0; j < m; j++) {
                sMap[s.charAt(i + j) - 'a']++;
//                 sMap.merge(sub.charAt(j), 1, Integer::sum);
            }
            if (Arrays.equals(pMap, sMap))ans.add(i);
            Arrays.fill(sMap, 0);
//            if(sMap.equals(pMap)) ans.add(i);
//             sMap.clear();
        }
        return ans;
    }
}