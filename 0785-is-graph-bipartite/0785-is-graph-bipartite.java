class Solution {
    public boolean isBipartite(int[][] graph) {
         int n = graph.length;
        int[] color = new int[n];
        for(int i = 0;i < n;i++){
            if(color[i] != 0) continue;
            color[i] = 1;
            Queue<Integer> q = new LinkedList<>();
            q.add(i);
            while(!q.isEmpty()){
                int cur = q.poll();
                for(int next : graph[cur]){
                    if(color[next] == 0){
                        color[next] = color[cur] == 1 ? 2 : 1;
                        q.add(next);
                    }else if(color[next] == color[cur]){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}