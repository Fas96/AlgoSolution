class Solution {
   public  int rob(int[] nums) {
        if (nums == null || nums.length == 0)return 0;
        return Math.max(robRange(nums, 1, nums.length - 1), nums[0] + robRange(nums, 2, nums.length - 2));
    }
    public  int robRange(int[] nums, int start, int end) {
        if (start > end)return 0;
        int max = 0;
        int noRob = 0;
        int rob = 0;
        for (int i = start; i <= end; i ++) {
            int newNoRob = Math.max(rob, noRob);
            int newRob = noRob + nums[i];
            rob = newRob;
            noRob = newNoRob;
            max = Math.max(max, rob);
            max = Math.max(max, noRob);
        }
        return max;
    }
}