class Solution {
    public int stoneGameII(int[] piles) {
        int[][] dp=new int[piles.length][piles.length]; 
        int[] suffixSum=new int[piles.length];
        
        if(piles.length==0)return 0;
        if(piles.length==1)return piles[0];
        
        suffixSum[piles.length-1]=piles[piles.length-1];
        for(int i=piles.length-2;i>=0;i--){
            suffixSum[i]=suffixSum[i+1]+piles[i];
        }
        return dfs(piles,0,1,dp,suffixSum);
    }

    private int dfs(int[] piles, int idx, int endIdx, int[][] dp, int[] suffixSum) {
        if(idx>=piles.length)return 0;
        if(dp[idx][endIdx]!=0)return dp[idx][endIdx];
        int max=Integer.MIN_VALUE;
        for(int i=1;i<=2*endIdx;i++){
            max=Math.max(max,suffixSum[idx]-dfs(piles,idx+i,Math.max(i,endIdx),dp,suffixSum));
        }
        dp[idx][endIdx]=max;
        return max;
    }
 
}