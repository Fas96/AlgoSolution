class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int N=edges.length;
        int[] node1Dist=new int[N];
        int[] node2Dist=new int[N];

        dilateInit(node1Dist, node2Dist);
        node1AndNode2Dist(edges, node1, node2, node1Dist, node2Dist);

        int answer=-1;
        int maxDist=Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            if (node1Dist[i] != -1 && node2Dist[i] != -1) {
                if (maxDist > Math.max(node1Dist[i], node2Dist[i])) {
                    maxDist = Math.max(node1Dist[i], node2Dist[i]);
                    answer = i;
                }
            }
        }
        return answer;

    }

    private void node1AndNode2Dist(int[] edges, int node1, int node2, int[] node1Dist, int[] node2Dist) {
        //node1
        int cur = node1;
        int step = 0;
        while (cur != -1 && node1Dist[cur] == -1) {
            node1Dist[cur] = step++;
            cur = edges[cur];
        }

        //node2
        cur = node2;
        step = 0;
        while (cur != -1 && node2Dist[cur] == -1) {
            node2Dist[cur] = step++;
            cur = edges[cur];
        }
    }

    private static void dilateInit(int[] node1Dist, int[] node2Dist) {
        Arrays.fill(node1Dist, -1);
        Arrays.fill(node2Dist, -1);
    }
}