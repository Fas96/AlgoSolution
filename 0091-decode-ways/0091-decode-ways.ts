function numDecodings(s: string): number {
    
 let n=s.length;
    let dp=new Array(n+1).fill(0);
    dp[n]=1;
    dp[n-1]=s[n-1]=="0"?0:1;
    for(let i=n-2;i>=0;i--){
        if(s[i]=="0"){
            continue;
        }
        dp[i]=dp[i+1]+(s[i]=="1"||s[i]=="2"&&s[i+1]<="6"?dp[i+2]:0);
    }
    console.log(dp);
    return dp[0];
};