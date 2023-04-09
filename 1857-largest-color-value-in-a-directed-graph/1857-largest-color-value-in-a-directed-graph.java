class Solution {
    public int largestPathValue(String colors, int[][] edges) {
         int n = colors.length();
        int m = edges.length;
        List<Integer>[] adj = new ArrayList[n];
        int[] indegree = new int[n];
        
        for (int i = 0; i < n; i++)  adj[i] = new ArrayList<>();
        
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            indegree[edge[1]]++;
        }
        
        int[][] freq = new int[n][26];
        
        for (int i = 0; i < n; i++)  freq[i][colors.charAt(i) - 'a']++;
        
        int max_cnt = 0;
        int vis = 0;
        Queue<Integer> qu = new LinkedList<>();
        
        
        for (int i = 0; i < n; i++)  if (indegree[i] == 0) qu.offer(i);
        
        while (!qu.isEmpty()) {
            int curr = qu.poll();
            vis++;
            for (int node : adj[curr]) {
                for (int i = 0; i < 26; i++)
                    freq[node][i] = Math.max(freq[node][i], freq[curr][i] + (colors.charAt(node) - 'a' == i ? 1 : 0));
                indegree[node]--;
                if (indegree[node] == 0)
                    qu.offer(node);
            }
            max_cnt = Math.max(max_cnt, Arrays.stream(freq[curr]).max().getAsInt());
        }
        return vis == n ? max_cnt : -1;
    }
    
}