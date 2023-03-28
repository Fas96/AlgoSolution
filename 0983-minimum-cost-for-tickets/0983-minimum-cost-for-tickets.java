class Solution {
    public int mincostTickets(int[] days, int[] costs) {
             int[] dp = new int[days.length];
          return mincostTicketsHelper(days, costs, 0, dp);
    }

    private int mincostTicketsHelper(int[] days, int[] costs, int i, int[] dp) {
        if (i >= days.length) return 0;
        if (dp[i] != 0) return dp[i];
        int j = i;
        int oneDayPass = costs[0] + mincostTicketsHelper(days, costs, i + 1, dp);
        while (j < days.length && days[j] < days[i] + 7) j++;
        int sevenDayPass = costs[1] + mincostTicketsHelper(days, costs, j, dp);
        while (j < days.length && days[j] < days[i] + 30) j++;
        int thirtyDayPass = costs[2] + mincostTicketsHelper(days, costs, j, dp);
        dp[i] = Math.min(oneDayPass, Math.min(sevenDayPass, thirtyDayPass));
        return dp[i];
    }
}