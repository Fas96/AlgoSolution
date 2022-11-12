class Solution {
    public int hIndex(int[] citations) {
        int N = citations.length;
        int[] count = new int[N+1];
        for (int c : citations) {
            if (c >= N) count[N]++;
            else count[c]++;
        }
        int sum = 0;
        for (int i = N; i >= 0; i--) {
            sum += count[i];
            if (sum >= i) return i;
        }
        return 0;
    }
}