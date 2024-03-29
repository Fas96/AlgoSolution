class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        int[] ans = new int[n];
        Arrays.sort(potions);

        for(int i=0; i<n; i++){
            int L = 0;
            int R = m - 1;
            while (L <= R) {
                int mid = L + (R - L) / 2;
                long product = (long) spells[i] * potions[mid];
                if (product >= success) R = mid - 1;
                else L = mid + 1;
            }
            ans[i] = m - L;
        }

        return ans;

    }
   
    /*TLE
    
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        int[] ans = new int[n];

        for(int i=0; i<n; i++){
            int cnt = 0;
            for(int j=0; j<m; j++){
                long x = (long) spells[i] *potions[j];
                if(x>=success)cnt++;
            }
            ans[i] = cnt;
        }
     
        return ans;
    }
    */
}