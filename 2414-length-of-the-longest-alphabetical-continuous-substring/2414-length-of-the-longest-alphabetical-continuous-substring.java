class Solution {
    public int longestContinuousSubstring(String s) {
        int start = 0, ans = 1;
        int N=s.length();
        char[] cArr=s.toCharArray();
        for (int i = 1; i < N; ++i) {
            if (cArr[i] != cArr[start] + i - start)
                start = i;
            ans = Math.max(ans, i - start + 1);
        }
        return ans;
    }
}