class Solution {
    public int numSubseq(int[] nums, int target) {
        int ans = 0;
        int MOD = (int) 1e9 + 7;
        int[] pow = new int[nums.length];
        pow[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            pow[i] = pow[i - 1] * 2 % MOD;
        }
        Arrays.sort(nums);
        int windowStart = 0, windowEnd = nums.length - 1;
        while (windowStart <= windowEnd) {
            if (nums[windowStart] + nums[windowEnd] > target) {
                windowEnd--;
            } else {
                ans = (ans + pow[windowEnd -windowStart]) % MOD;
                windowStart++;
            }
        }
        return ans;
    }
}