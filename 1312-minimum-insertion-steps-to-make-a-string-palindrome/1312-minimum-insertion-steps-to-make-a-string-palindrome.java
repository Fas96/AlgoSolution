class Solution {
    public int minInsertions(String s) {
         int n=s.length();
        int[][] dp=new int[n][n];
        for (int i = n-1; i >=0 ; i--) {
            for (int j = i+1; j <n ; j++) {
                if(s.charAt(i)==s.charAt(j)){
                    dp[i][j]=dp[i+1][j-1];
                }else{
                    dp[i][j]=Math.min(dp[i+1][j],dp[i][j-1])+1;
                }
            }
        }
        return dp[0][n-1];
    }
}