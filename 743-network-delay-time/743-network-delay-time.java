class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
         int res=0;
    Map<Integer, List<int[]>> uv= new HashMap<>();

    //node and the connected  target weight
    for (int [] time:times) {
      int src=time[0],target=time[1], weight=time[2];
      if(!uv.containsKey(src)){
        uv.put(src,new LinkedList<>());
      }
      uv.get(src).add(new int[]{target,weight});
    }
    //sorts the weights
    Queue<int[]> minHeap= new PriorityQueue<>((w1,w2)->w1[1]-w2[1]);
    Set<Integer> visitedNode= new HashSet<>();

    //starting edge
    minHeap.add(new int[]{k,0});

    //BFS
    while (!minHeap.isEmpty()){
      int[] curNode = minHeap.poll();
      int curSrc=curNode[0],curWeight=curNode[1];
      if(visitedNode.contains(curSrc)) continue;
      res=curWeight;
      visitedNode.add(curSrc);
      if(!uv.containsKey(curSrc))continue;
      for (int[] edge:uv.get(curSrc)){
        int tar=edge[0],tarWeight=edge[1];
        minHeap.add(new int[]{tar,curWeight+tarWeight});
      }
    }

    return  visitedNode.size()==n?res:-1;
    }
}