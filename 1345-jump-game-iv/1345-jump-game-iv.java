class Solution {
    public int minJumps(int[] arr) {
         int n= arr.length;
        if(n==1) return 0;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int i=0;i<n;i++){
            map.computeIfAbsent(arr[i], t->new ArrayList<>()).add(i);
        }
        boolean[] visited = new boolean[n];
        visited[0] = true;
        int[] dist = new int[n];
        dist[0] = 0;
        List<Integer> queue = new ArrayList<>();
        queue.add(0);
        while(!queue.isEmpty()){
            int u = queue.remove(0);
            if(u==n-1) return dist[u];
            if(u-1>=0 && !visited[u-1]){
                visited[u-1] = true;
                dist[u-1] = dist[u]+1;
                queue.add(u-1);
            }
            if(u+1<n && !visited[u+1]){
                visited[u+1] = true;
                dist[u+1] = dist[u]+1;
                queue.add(u+1);
            }
            for(int v: map.getOrDefault(arr[u], new ArrayList<>())){
                if(!visited[v]){
                    visited[v] = true;
                    dist[v] = dist[u]+1;
                    queue.add(v);
                }
            }
            map.remove(arr[u]);
        }
        return -1;
    }
}