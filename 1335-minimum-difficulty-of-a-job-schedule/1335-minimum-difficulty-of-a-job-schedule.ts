function minDifficulty(jobDifficulty: number[], d: number): number {

      let n = jobDifficulty.length;
    if (n < d) {
        return -1;
    }
    let dp = new Array(d);
    
    for (let i = 0; i < d; i++) {
        dp[i] = new Array(n);
        
    }
    dp[0][0] = jobDifficulty[0];
    for (let i = 1; i < n; i++) {
        dp[0][i] = Math.max(dp[0][i - 1], jobDifficulty[i]);
        
    }
    for (let i = 1; i < d; i++) {
        for (let j = i; j < n; j++) {
            let max = 0;
            dp[i][j] = Number.MAX_SAFE_INTEGER;
            for (let k = j; k >= i; k--) {
                max = Math.max(max, jobDifficulty[k]);
                dp[i][j] = Math.min(dp[i][j], dp[i - 1][k - 1] + max);
            }
        }
    }
    return dp[d - 1][n - 1];
};