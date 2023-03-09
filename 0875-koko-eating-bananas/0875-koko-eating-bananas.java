class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
     int low = 1, high = 1_000_000_000;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (checkIfCanEatAll(piles, h, mid)) high = mid;
            else low = mid + 1;
        }
        return low;

    }

    private boolean checkIfCanEatAll(int[] piles, int h, int mid) {
        int sum = 0;
        for (int pile : piles) {
            sum += (pile / mid + (pile % mid == 0 ? 0 : 1));
        }
        return sum <= h;
    }
}