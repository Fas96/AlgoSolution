class Solution {
    public int minimizeArrayValue(int[] nums) {
        long sum = 0;
        long max = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, ((sum+=nums[i])+i)/(i+1));
        }

        return (int)max;
    }
}