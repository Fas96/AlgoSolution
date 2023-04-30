class Solution {
   public int maxNumEdgesToRemove(int n, int[][] edges) {
        UF a = new UF(n + 1);
        UF b = new UF(n + 1);
        int extra = 0;
        for (int[] e: edges) {
            if (e[0] != 3) continue;
            boolean ext = false;
            if (!a.add(e)) ext = true;
            if (!b.add(e)) ext = true;
            if (ext) extra++;
        }
        for (int[] e: edges) {
            if (e[0] == 1 && !a.add(e)) extra++;
            if (e[0] == 2 && !b.add(e)) extra++;
        }
        return a.isConnected() && b.isConnected() ? extra : -1;
    }
}

class UF {
    int[] nodes;
    int edjCnt = 0;
    UF(int n) {
        nodes = new int[n];
        for(int i = 0; i < n; i++)
            nodes[i] = i;
    }
    
    boolean isConnected() {
        return (nodes.length - 1 - 1) == edjCnt;
    }
    
    boolean add(int[] edj) {
        int aHead = head(edj[1]);
        int bHead = head(edj[2]);
        if (aHead != bHead) {
            nodes[bHead] = aHead;
            edjCnt++;
            return true;
        }
        return false;
    }
    
    int head(int n) {
        if (n != nodes[n]) 
            nodes[n] = head(nodes[n]);
        return nodes[n];
    }
}