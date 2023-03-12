class Solution {
    public int nthUglyNumber(int n) {
        TreeSet<Long> set = new TreeSet<>();
        set.add(1L);
        for (int i = 1; i < n; i++) {
            long poll = set.pollFirst();
            set.add(poll * 2);
            set.add(poll * 3);
            set.add(poll * 5);
        }
        return set.first().intValue();
    }
}