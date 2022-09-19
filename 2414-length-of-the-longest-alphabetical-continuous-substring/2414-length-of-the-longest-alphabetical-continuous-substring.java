class Solution {
    public int longestContinuousSubstring(String s) {
           int N = 0, ans = 1;
        char[] cArr=s.toCharArray();
        for (int i = 1; i < s.length(); ++i) {
            if (cArr[i] != cArr[N] + i - N)
                N = i;
            ans = Math.max(ans, i - N + 1);
        }
        return ans;
    }
}