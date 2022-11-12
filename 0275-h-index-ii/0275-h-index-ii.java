class Solution {
    public int hIndex(int[] citations) {
        int N = citations.length;
        int L = 0, R = N - 1;
        while (L <= R) {
            int M = (L + R) / 2;
            if (citations[M] == N - M) {
                return N - M;
            } else if (citations[M] > N - M) {
                R = M - 1;
            } else {
                L = M + 1;
            }
        }
        return N - L;
    }
}