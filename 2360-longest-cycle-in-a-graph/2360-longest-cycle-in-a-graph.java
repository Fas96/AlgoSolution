class Solution {
   public int longestCycle(int[] edges) {
        int n = edges.length;
        int[] inDegree = new int[n]; 
        ArrayList <Integer>[] adjList = new ArrayList[n];
        for(int i = 0; i < n; i++) adjList[i] = new ArrayList <Integer>();
        

        for(int i = 0; i < n; i++)
        {
            int u = i;
            int v = edges[i];      

            if(v != - 1)  
            {
                adjList[u].add(v); 
                inDegree[v] += 1;  
            }
        }

        Queue <Integer> q = new LinkedList<>();
        int cycle = -1;
        boolean[] vis = new boolean[n];

        for(int i = 0; i < n; i++)
        {
            if(inDegree[i] == 0) {
                q.add(i);
                vis[i] = true; 
            }
        }

        while(q.size() > 0) 
        {
            int u = q.poll();

            for(int i = 0; i < adjList[u].size(); i++)
            {
                int v = adjList[u].get(i); 
                inDegree[v] -= 1;  

                if(inDegree[v] == 0)
                {
                    q.add(v); 
                    vis[v] = true;  
                }
            }
        }
      
        for(int i = 0; i < n; i++)
        { 
            if(!vis[i]) 
            {
                cycle = Math.max(cycle, dfs(adjList, vis, i));  
            }   
        }

        return cycle; 
    }

    public int dfs(ArrayList <Integer>[] adjList, boolean[] vis, int node)
    {

        if(vis[node])
        {
            return  0;
        }

        int nodeCount = 1;
        vis[node] = true;

        for(int i = 0; i < adjList[node].size(); i++)
        {
            int v = adjList[node].get(i);

            if(vis[v] == false)
            {
                nodeCount += dfs(adjList, vis, v);
            }
        }

        return nodeCount;
    }
}