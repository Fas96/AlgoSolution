class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        
         List<Node> [] map= new ArrayList[n];
        int answer=0;

        for (int i = 0; i < map.length; i++) {
            map[i] = new ArrayList<>();
        }

        for (int[] flight : flights) {
            int from = flight[0], to = flight[1], price = flight[2];
            map[from].add(new Node(to,0 ,price));
        }



        int[] prices = new int[n];
        int[] stops = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        Arrays.fill(stops, Integer.MAX_VALUE);

        prices[src] = 0;
        stops[src] = 0;

        PriorityQueue<Node> heap = new PriorityQueue<>((n1, n2) -> Integer.compare(n1.cost, n2.cost));

        heap.add(new Node(src, 0, 0));


        while (!heap.isEmpty()){
            Node curNode= heap.poll();
            if (curNode.src == dst) return curNode.cost;
            if (curNode.dest > k) continue;
            for (Node neighbor : map[curNode.src]) {
                int nextCost = curNode.cost + neighbor.cost;
                int nextStop = curNode.dest+1;
                if (prices[neighbor.src] > nextCost) {
                    prices[neighbor.src] = nextCost;
                    stops[neighbor.src] = nextStop;
                    heap.add(new Node(neighbor.src, nextStop, nextCost));
                } else if (stops[neighbor.src] > curNode.dest) {
                    heap.add(new Node(neighbor.src, nextStop, nextCost));
                }
            }
        }

        answer=prices[dst] == Integer.MAX_VALUE ? -1 : prices[dst];

        return answer;
    }
    class Node{
        public int src;
        public int dest;
        public int cost;
        public Node(int src,int dest,int cost){
            this.src=src;
            this.dest=dest;
            this.cost=cost;
        }


    }
}