/*

 long[] dp = new long[s.length + 1];
        dp[0] = startFuel;
        for (int i = 0; i < s.length; ++i)
            for (int t = i; t >= 0 && dp[t] >= s[i][0]; --t)
                dp[t + 1] = Math.max(dp[t + 1], dp[t] + s[i][1]);
        for (int t = 0; t <= s.length; ++t)
            if (dp[t] >= target) return t;
        return -1;
*/
class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
       int n = stations.length;
        int stops = 0, distance=0;
        
        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i=0; i<=n; i++) {
            int pos = target, fuel = 0;
            if (i < n) {
                pos = stations[i][0];
                fuel = stations[i][1];
            }
            
            startFuel -= pos - distance;
            distance = pos;
            
            while (startFuel < 0 && !pq.isEmpty()) {
                startFuel += pq.poll();
                stops++;
            }
            
            if (startFuel < 0) return -1;
            if (distance >= target) return stops;
            
            pq.add(fuel);
        }
        
        return -1;  
    }
}