class Solution {
    public int minDistance(String word1, String word2) { 
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (isSameCharacter(word1, word2, i, j)) diagonalValue(dp, i, j);
                else minOfTDL(dp, i, j);
            }
        }
        return dp[m][n];
    }

    private   void minOfTDL(int[][] dp, int i, int j) {
        dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
    }

    private   void diagonalValue(int[][] dp, int i, int j) {
        dp[i][j] = dp[i - 1][j - 1];
    }

    private   boolean isSameCharacter(String word1, String word2, int i, int j) {
        return word1.charAt(i - 1) == word2.charAt(j - 1);
    }
}