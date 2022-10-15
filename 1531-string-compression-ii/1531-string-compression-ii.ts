 
function getLengthOfOptimalCompression(s: string, k: number): number {
       let n = s.length;
    let dp = new Array(110);
    for (let i = 0; i <= n; i++) {
        dp[i] = new Array(110);
        for (let j = 0; j <= n; j++) {
            dp[i][j] = 9999;
        }
        
    }
    // for (int[] i : dp) Arrays.fill(i, n); // this is a bit slower (100ms)
    dp[0][0] = 0;
    for(let i = 1; i <= n; i++) {
        for(let j = 0; j <= k; j++) {                
            let cnt = 0, del = 0;
            for(let l = i; l >= 1; l--) { // keep s[i], concat the same, remove the different
                if(s.charAt(l - 1) == s.charAt(i - 1)) cnt++;
                else del++;
                if(j - del >= 0) 
                    dp[i][j] = Math.min(dp[i][j], 
                                        dp[l-1][j-del] + 1 + (cnt >= 100 ? 3 : cnt >= 10 ? 2 : cnt >= 2 ? 1: 0));
            }
            if (j > 0) // delete s[i]
                dp[i][j] = Math.min(dp[i][j], dp[i-1][j-1]);
        }
    }
    return dp[n][k];
   

};