class Solution {
    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
        
      int n = nums1.length;
        int[] sorted = nums1.clone();
        Arrays.sort(sorted);
        int MOD = 1000000007;
        int sum = 0;
        int maxDiff = 0;
        for (int i = 0; i < n; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            sum = (sum + diff) % MOD;
            int j = binarySearch(sorted, nums2[i]);
            if (j < n) {
                maxDiff = Math.max(maxDiff, diff - (sorted[j] - nums2[i]));
            }
            if (j > 0) {
                maxDiff = Math.max(maxDiff, diff - (nums2[i] - sorted[j - 1]));
            }
        }
        return (sum - maxDiff + MOD) % MOD;

    }

    public int binarySearch(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        if (target > nums[high]) {
            return high + 1;
        }
        while (low < high) {
            int mid = (high - low) / 2 + low;
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}