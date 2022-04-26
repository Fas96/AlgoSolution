class Solution {
    public int minCostConnectPoints(int[][] points) {
        
        int n = points.length;
        PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->a[0]-b[0]);
        boolean[] connected = new boolean[n];
        connected[0] = true;
        fill(points,q,connected,0);
        int res = 0;
        int count = 1;
        while(count<n){
            int a[] = q.poll();
            assert a != null;
            if(connected[a[1]]) continue;
            res+=a[0];
            connected[a[1]] = true;
            fill(points,q,connected,a[1]);
            count++;
        }
        return res;
      
    }
    int dist(int a[], int b[]){
        return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);
    }

    void fill(int points[][], PriorityQueue<int[]> q, boolean connected[], int idx){
        int n = connected.length;
        for(int i = 0 ; i<n ; i++){
            if(!connected[i]){
                q.add( new int[]{dist(points[i],points[idx]),i});
            }
        }
    }
}