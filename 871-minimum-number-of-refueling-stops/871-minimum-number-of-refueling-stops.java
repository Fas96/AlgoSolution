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