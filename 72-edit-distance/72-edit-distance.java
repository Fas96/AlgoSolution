class Solution {
    public int minDistance(String word1, String word2) {
        
    int M=word1.length();
    int N=word2.length();
    int[][] dp= new int[N+1][M+1];
    for (int i = 0; i <= N; i++) {
      dp[i][0]=i;
    }
    for (int i = 0; i <=M; i++) {
      dp[0][i]=i;
    }
    for (int i = 1; i < N+1; i++) {
      for (int j = 1; j < M+1; j++) {
        if(word1.charAt(j-1)==word2.charAt(i-1)){
          dp[i][j]=dp[i-1][j-1];
        }else {
          dp[i][j]=Math.min(dp[i-1][j-1],Math.min(dp[i][j-1],dp[i-1][j]))+1;
        }
      }

    }

    return  dp[N][M];
    }
}