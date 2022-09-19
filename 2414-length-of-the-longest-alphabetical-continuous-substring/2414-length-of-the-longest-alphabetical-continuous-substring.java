class Solution {
    public int longestContinuousSubstring(String s) {
           int j = 0, res = 1;
        char[] cArr=s.toCharArray();
        for (int i = 1; i < s.length(); ++i) {
            if (cArr[i] != cArr[j] + i - j)
                j = i;
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}