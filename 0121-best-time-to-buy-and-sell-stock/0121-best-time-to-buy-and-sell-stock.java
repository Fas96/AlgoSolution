class Solution {
    public int maxProfit(int[] prices) {
                int N=prices.length;
        if(N==0)return 0;
        int  maxProfit=0;
        int minSofar=prices[0];
        for (int a : prices) {
            maxProfit=Math.max(maxProfit,a-minSofar);
            minSofar=Math.min(minSofar,a);
        }

        return maxProfit;
    }
}