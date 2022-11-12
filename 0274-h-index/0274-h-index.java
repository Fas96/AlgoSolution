
import static java.util.Arrays.sort;
class Solution {
    public int hIndex(int[] citations) {
         Arrays.sort(citations);
        int N = citations.length;
        int res = 0;
        for (int i = 0; i < N; i++) {
            if (citations[i] >= N - i) {
                res = N - i;
                break;
            }
        }
        return res;
    }
}