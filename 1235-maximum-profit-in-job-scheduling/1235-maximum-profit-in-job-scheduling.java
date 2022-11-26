class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
         int N = startTime.length;
        List<Pair> pairJobSchedulingList = new ArrayList<>();
        for (int i = 0; i < N; ++i)
            pairJobSchedulingList.add(new Pair(i,startTime[i], endTime[i], profit[i]));
        pairJobSchedulingList.sort((a, b) -> a.endTime - b.endTime);
        TreeMap<Integer, Integer> orderProfit = new TreeMap<>();
        orderProfit.put(0, 0);
        for (Pair pair : pairJobSchedulingList) {
            int cur = orderProfit.floorEntry(pair.startTime).getValue() + pair.profit;
            if (cur > orderProfit.lastEntry().getValue())
                orderProfit.put(pair.endTime, cur);
        }
        return orderProfit.lastEntry().getValue();

    }
    private class Pair {
        int index;
        int startTime;
        int endTime;
        int profit;

public Pair(int index, int startTime, int endTime, int profit) {
            this.index = index;
            this.startTime = startTime;
            this.endTime = endTime;
            this.profit = profit;
        } 
    }
}