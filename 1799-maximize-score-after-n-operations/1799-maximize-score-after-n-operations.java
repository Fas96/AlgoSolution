class Solution {
    public int maxScore(int[] nums) {
        var memo = new Integer[1<<14];
        int n = nums.length;
        return dfs(nums,n/2,(1<<n)-1,memo);
    }
    
    int dfs(int[]nums,int k,int mask,Integer[]memo){
        if (k == 0){
            return 0;
        }
        if (memo[mask] != null){
            return memo[mask];
        }
        int n = nums.length, ans = 0;
        for(int i = 0; i+1 < n; ++i){
            for(int j = i+1; j < n; ++j){
                int win = (n/2-k+1)*gcd(nums[i],nums[j]);
                if ((mask&(1<<i)) != 0
                   && (mask&(1<<j)) != 0){
                    ans = Math.max(ans,win+dfs(nums,k-1,mask^(1<<i)^(1<<j),memo));
                }
            }
        }
        return memo[mask] = ans;
    }
    
    int gcd(int a, int b){
        return b == 0 ? a : gcd(b,a%b);
    }
}