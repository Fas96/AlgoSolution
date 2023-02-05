class Solution {
    public List<Integer> findAnagrams(String s, String p) {
         int n = s.length();
        int m = p.length();

        int[] pMap = new int[26];
        int[] sMap = new int[26]; 

        for (Character c : p.toCharArray()) {
            pMap[c - 'a']++; 
        }

        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i <= n - m; i++) { 
            for (int j = 0; j < m; j++) {
                sMap[s.charAt(i + j) - 'a']++; 
            }
            if (Arrays.equals(pMap, sMap))ans.add(i);
            Arrays.fill(sMap, 0); 
        }
        return ans;
    }
}