class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        Integer[][] dp= new Integer[1000][1000];
        return  memo(nums,multipliers,0,0,nums.length-1,dp);
    }

    private int memo(int[] nums, int[] multipliers, int L, int R, int N, Integer[][] dp) {
        if(L == multipliers.length)
            return 0;
        if(dp[R][L] != null)
            return dp[R][L];
        int leftSide = nums[R] * multipliers[L] + memo(nums, multipliers, L + 1, R + 1, N, dp);
        int rightSide = nums[N] * multipliers[L] + memo(nums, multipliers, L + 1, R, N - 1, dp);
        dp[R][L] = Math.max(leftSide, rightSide);
        return dp[R][L];
        
    }
}