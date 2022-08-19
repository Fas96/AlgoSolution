class Solution {
  public int longestCommonSubsequence(String text1, String text2) {
    int M=text1.length();
    int N=text2.length();
    int[][] dp= new int[M+1][N+1];
    for (int i = 1; i <=M; i++) {
      for (int j = 1; j <=N; j++) {
        if(text1.charAt(i-1)==text2.charAt(j-1)){
          dp[i][j]=+1+dp[i-1][j-1];
        }else{
          dp[i][j]= Math.max(dp[i][j-1],dp[i-1][j]);
        }
      }
    }
    return dp[M][N];
  }
}