class SmallestInfiniteSet {

   PriorityQueue<Integer> pq = null;

        public SmallestInfiniteSet() {
            pq=new PriorityQueue<>((a, b) -> a - b);
            for (int i = 0; i < 1_000; i++) {
                pq.offer(i+1);
                
            }
        }

        public int popSmallest() {
            return  pq.poll();
        }

        public void addBack(int num) {
            if(pq.contains(num))
                return;
            pq.add(num);
        }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */