class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        int[][] dp= new int[1000][1000];
        return  memo(nums,multipliers,0,0,nums.length-1,dp);
    }

    private int memo(int[] nums, int[] multipliers, int L, int R, int N, int[][] dp) {
        if(L == multipliers.length)
            return 0;
        if(dp[R][L] != 0)
            return dp[R][L];
        int lf = nums[R] * multipliers[L] + memo(nums, multipliers, L + 1, R + 1, N, dp);
        int rg = nums[N] * multipliers[L] + memo(nums, multipliers, L + 1, R, N - 1, dp);
        dp[R][L] = Math.max(lf, rg);
        return dp[R][L];
        
    }
}