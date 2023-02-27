class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
         int maxDistance = 0;
        int m = nums1.length, n = nums2.length;
        int i = 0, j = 0;
        while (i < m  && j < n) {
            if (nums1[i] <= nums2[j]) {
                maxDistance = Math.max(maxDistance, j - i);
                j++;
            } else {
                i++;
            }
        }
        return maxDistance;
    }
}