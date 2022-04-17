class Solution {
    public int maxProfit(int[] prices) {
        int sell=Integer.MIN_VALUE;
        int buy=prices[0];

        if(prices.length<=1)return 0;


        for (int i = 0; i < prices.length; i++) {
               buy=Math.min(buy,prices[i]);
            sell= Math.max(sell,prices[i]-buy);

        }

        return sell;
    }
}