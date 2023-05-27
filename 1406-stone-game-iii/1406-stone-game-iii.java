class Solution {
    public String stoneGameIII(int[] stoneValue) {
   int[] dp=new int[stoneValue.length+1];
        int[] suffixSum=new int[stoneValue.length+1];
        suffixSum[stoneValue.length]=0;
        for(int i=stoneValue.length-1;i>=0;i--){
            suffixSum[i]=suffixSum[i+1]+stoneValue[i];
        }
        int max=dfs(stoneValue,0,dp,suffixSum);
        if(max>suffixSum[0]-max){
            return "Alice";
        }else if(max<suffixSum[0]-max){
            return "Bob";
        }else{
            return "Tie";
        }
        

    }

    private int dfs(int[] stoneValue, int i, int[] dp, int[] suffixSum) {
        if(i>=stoneValue.length)return 0;
        if(dp[i]!=0)return dp[i];
        int max=Integer.MIN_VALUE;
        for(int j=1;j<=3;j++){
            max=Math.max(max,suffixSum[i]-dfs(stoneValue,i+j,dp,suffixSum));
        }
        dp[i]=max;
        return max;
    }
}