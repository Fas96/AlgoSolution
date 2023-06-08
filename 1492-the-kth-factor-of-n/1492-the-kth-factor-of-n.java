class Solution {
    public int kthFactor(int n, int k) {
        List<Integer> factors=new LinkedList<>();
        for (int i = 1; i <=n; i++) {
            if(n%i==0)factors.add(i);
        }
        return k>factors.size()?-1:factors.get(k-1);
    }
}