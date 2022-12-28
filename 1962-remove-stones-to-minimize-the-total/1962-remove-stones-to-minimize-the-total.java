class Solution {
    public int minStoneSum(int[] piles, int k) {
     PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int pile : piles) {
            pq.add(pile);
        }
        while (k-- > 0) {
            int max = pq.poll();
            pq.add(max - max / 2);
        }
        int res = 0;
        while (!pq.isEmpty()) {
            res += pq.poll();
        }
        return res;
         
    }
}