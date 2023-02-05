class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int n = s.length();
        int m = p.length();

        int[] pCount = new int[26];
        int[] sCount = new int[26];

        for (int i = 0; i < m; i++) {
            pCount[p.charAt(i) - 'a']++;
        }

        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i <= n - m; i++) {
            for (int j = 0; j < m; j++) {
                sCount[s.charAt(i + j) - 'a']++;
            }
            if (Arrays.equals(pCount, sCount)) {
                ans.add(i);
            }
            Arrays.fill(sCount, 0);
        }
        return ans;
    }
}