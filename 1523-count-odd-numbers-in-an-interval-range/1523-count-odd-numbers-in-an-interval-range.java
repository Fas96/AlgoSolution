class Solution {
    public int countOdds(int low, int high) {
        int ans = 0;
        if(low % 2 == 0) low++;
        if(high % 2 == 0) high--;
        ans = (high - low) / 2 + 1;
        return ans;
    }
}