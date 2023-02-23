class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        
        PriorityQueue<IPO> capitalPq = new PriorityQueue<>((a, b) -> a.capital - b.capital);
        IPOBuilder(profits, capital, capitalPq);
        PriorityQueue<IPO> profitPq = new PriorityQueue<>((a, b) -> b.profit - a.profit);
        for (int i = 0; i < k; i++) {
            while (hasEnoughCapital(w, capitalPq)) {
                profitPq.offer(capitalPq.poll());
            }
            if (profitPq.isEmpty()) break;
            
            w += profitPq.poll().profit;
        }
        return w;

    }

    private static boolean hasEnoughCapital(int w, PriorityQueue<IPO> capitalPq) {
        return !capitalPq.isEmpty() && capitalPq.peek().capital <= w;
    }

    private  void IPOBuilder(int[] profits, int[] capital, PriorityQueue<IPO> capitalPq) {
        for (int i = 0; i < profits.length; i++) {
            capitalPq.offer(new IPO(profits[i], capital[i]));
        }
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