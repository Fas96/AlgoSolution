class Solution {
    public int maxProfit(int[] prices) {
      
        return dpHelper(0,prices,0,new Integer[prices.length][2]);
    }
    public int dpHelper(int index, int[] prices, int buyOrSell, Integer[][] dp)
    {
        if(index >=prices.length)
            return 0;
        if(dp[index][buyOrSell]!= null)
            return dp[index][buyOrSell];
        int result;
        if(buyOrSell==0)
        {
            result = Math.max(dpHelper(index+1, prices,buyOrSell,dp),dpHelper(index+1, prices,1,dp)-prices[index]);
        }
        else{
            result = Math.max(dpHelper(index+1, prices,buyOrSell,dp),dpHelper(index+2, prices,0,dp)+prices[index]);
        }
        return dp[index][buyOrSell] = result;
    }
}