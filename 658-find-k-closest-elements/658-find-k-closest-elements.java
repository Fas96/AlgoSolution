class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<int[]> pq= new PriorityQueue<>((o1,o2)->o2[0]!=o1[0] ? o2[0] - o1[0] : o2[1] - o1[1]);

        for (int a : arr) {
            pq.offer(new int[]{Math.abs(a-x), a});
            if(pq.size()>k)pq.poll();
        }

        List<Integer> res = pq.stream().map(e->e[1]).collect(Collectors.toList());
        Collections.sort(res);
       return res;
    }
}