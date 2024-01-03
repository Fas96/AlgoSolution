class Solution {
    public int numberOfBeams(String[] bank) { 
         int ans = 0;
        int prev = 0;

        for (String beam : bank) {
            int res = countOnes(beam);
            if (res > 0) {
                ans += prev * res;
                prev = res;
            }
        }

        return ans;
    }

    private static int countOnes(String beam) {
        int count = 0;
        for (char bit : beam.toCharArray()) {
            if (bit == '1') {
                count++;
            }
        }
        return count;
    }
}