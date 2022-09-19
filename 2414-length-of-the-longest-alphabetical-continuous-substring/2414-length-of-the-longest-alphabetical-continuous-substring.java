class Solution {
    public int longestContinuousSubstring(String s) {
           int start = 0, ans = 1;
        char[] cArr=s.toCharArray();
        for (int i = 1; i < s.length(); ++i) {
            if (cArr[i] != cArr[start] + i - start)
                start = i;
            ans = Math.max(ans, i - start + 1);
        }
        return ans;
    }
}