class Solution {
    public int maxProfit(int[] prices) {
           int max=Integer.MIN_VALUE;
         

        if(prices.length<=1)return 0;
         int buy=prices[0];
        for (int i = 0; i < prices.length; i++) {
            buy =Math.min(buy,prices[i]);
            //for (int j = i; j < prices.length; j++) {
               max= Math.max(prices[i]-buy,max);
                
            //}//
             
        }
        return max;
    }
}