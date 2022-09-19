class Solution {
    public int longestContinuousSubstring(String s) {
         int start = 0, ans = 1;
        int N=s.length();
        int R=1;
        char[] cArr=s.toCharArray();
        while (R<N){
            if (cArr[R] != cArr[start] + R - start)
                start = R;
            ans = Math.max(ans, R - start + 1);
            R++;
        }
         
        return ans;
    }
}