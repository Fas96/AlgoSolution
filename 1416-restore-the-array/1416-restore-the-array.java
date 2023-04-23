class Solution {
    public int numberOfArrays(String s, int k) {
        int MOD=1_000_000_007;
        long[] dp = new long[s.length()+1];
        int len = String.valueOf(k).length();
        dp[0] = 1;
        for (int i = 1; i <= s.length(); i++) { 
            for (int j = i - 1; j >= 0 && i-j <= len; j--) {
                if (s.charAt(j)=='0') continue; 
                String sub = s.substring(j, i); 
                long n = Long.parseLong(sub);
                if (n > k) continue;
                dp[i] += dp[j];
                dp[i] %= MOD;
            }
        }
        return (int)dp[s.length()];
    }
}