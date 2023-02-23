class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        
      PriorityQueue<IPO> pq = new PriorityQueue<>((a, b) -> a.capital - b.capital);
        for (int i = 0; i < profits.length; i++) {
            pq.offer(new IPO(profits[i], capital[i]));
        }
        PriorityQueue<IPO> pq2 = new PriorityQueue<>((a, b) -> b.profit - a.profit);
        for (int i = 0; i < k; i++) {
            while (!pq.isEmpty() && pq.peek().capital <= w) {
                pq2.offer(pq.poll());
            }
            if (pq2.isEmpty()) {
                break;
            }
            w += pq2.poll().profit;
        }
        return w;

    }
    class IPO {
        int profit;
        int capital;
        public IPO(int profit, int capital) {
            this.profit = profit;
            this.capital = capital;
        }
    }
}