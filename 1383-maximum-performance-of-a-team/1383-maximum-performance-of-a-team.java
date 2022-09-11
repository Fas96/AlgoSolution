class Solution {
   public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        List<int[]> swers=new ArrayList<>();
        for(int i = 0; i < n; i++)
            swers.add(new int[]{speed[i], efficiency[i]});
        swers.sort((a, b) -> b[1] - a[1]);
        PriorityQueue<int[]> curTeam = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        long teamSpeed = 0;
        long maxPerformance = Long.MIN_VALUE;

        for (int[] cur : swers) {
            if(curTeam.size() == k){
                int[] slowGuy = curTeam.poll();
                assert slowGuy != null;
                teamSpeed -= slowGuy[0];
            }
            curTeam.add(cur);
            teamSpeed += cur[0];

            long performanceWithNewGuy = teamSpeed * (long) cur[1];
            maxPerformance = Math.max(maxPerformance, performanceWithNewGuy);

        }
        return (int) (maxPerformance % (int) (1e9 + 7));
    }
}