class Solution {
    public int findKthLargest(int[] nums, int k) {
            return quickSelect(nums, 0, nums.length - 1, nums.length - k);
        }
        private int quickSelect(int[] nums, int l, int r, int k) {
            int p = partition(nums, l, r);
            if (p < k) return quickSelect(nums, p + 1, r, k);
            if (p > k) return quickSelect(nums, l, p - 1, k);
            return nums[p];
        }
        private int partition(int[] nums, int l, int r) {
            int pivot = nums[r];
            int p = r;
            for (int i = l; i < p; i++) {
                if (nums[i] > pivot) {
                    swap(nums, i, p - 1);
                    swap(nums, p, p - 1);
                    i--;
                    p--;
                }
            }
            return p;
        }
        private void swap(int[] nums, int a, int b) {
            int tmp = nums[a];
            nums[a] = nums[b];
            nums[b] = tmp;
        }
}