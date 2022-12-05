class Solution {
    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
          int MOD = 1000000007;
        int absSum = 0,N = nums1.length;
        int[]diffArr = new int[N];
        for (int i = 0; i < N; i++) {
            absSum = (absSum + Math.abs(nums1[i] - nums2[i])) % MOD;
            diffArr[i] = Math.abs(nums1[i] - nums2[i]);
        }
        int maxDiff = 0;
        int[] sorted = nums1.clone();
        Arrays.sort(sorted);

        for (int i = 0; i < N; i++) {
            int j = binarySearch(sorted, nums2[i]);
            if (j < N) {
                maxDiff =  Math.max(maxDiff, diffArr[i] - (sorted[j] - nums2[i])) ;
            }
            if (j > 0) {
                maxDiff = Math.max(maxDiff, diffArr[i] - (nums2[i] - sorted[j - 1]));
            }
        }

        return (absSum - maxDiff +MOD) % MOD;
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