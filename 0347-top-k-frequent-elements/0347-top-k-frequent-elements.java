class Solution {
    public int[] topKFrequent(int[] nums, int k) {
      Map<Integer, Integer> map = new java.util.HashMap<>();
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
       PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(map::get));
        
        for(int key : map.keySet()){
            pq.offer(key);
            if(pq.size() > k) pq.poll();
        }
        int[] res = new int[k];
        for(int i = 0;i < k;i++){
            res[i] = pq.poll();
        }
        return res;
    }
    
}