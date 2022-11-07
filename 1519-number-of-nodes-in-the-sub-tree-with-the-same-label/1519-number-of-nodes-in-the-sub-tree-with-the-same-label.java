class Solution {
  public int[] countSubTrees(int n, int[][] edges, String labels) {
          int res[]=new int[n];

        //build graph
        List<Integer> graph[]=new ArrayList[n];
        for(int i=0;i<n;i++){
            graph[i]=new ArrayList<>();
        }
        for(int[] edge:edges){
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        boolean[] visited=new boolean[n];
        dfs(graph,visited,labels,res,0);
        return res;
    }

    private int[] dfs(List<Integer>[] graph, boolean[] visited, String labels, int[] res, int i) {
        visited[i]=true;
        int[] count=new int[26];

        count[labels.charAt(i)-'a']++;

        for(int j:graph[i]){
            if(!visited[j]){
                int freq[]=dfs(graph,visited,labels,res,j);
                for(int k=0;k<26;k++) {
                    count[k] += freq[k];
                }

            }
        }
        res[i]=count[labels.charAt(i)-'a'];
        return count;
    }
}