class Solution {
    public int kthSmallest(int[][] matrix, int k) {
      int ans=0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> o1-o2);

        for (int []a:matrix) {
            for (int n : a) {
                pq.add(n);
            }
        }
        while (k-->0){
            ans=pq.poll();
        }
        return ans;  
    }
}