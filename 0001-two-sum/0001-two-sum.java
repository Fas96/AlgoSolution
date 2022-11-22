class Solution {
    public int[] twoSum(int[] nums, int target) {
            int N= nums.length;
        for (int i = 0; i <N; i++) {
            for (int j = 0; j < N; j++) {
                   if (i==j) continue;
                 if(nums[i]+nums[j]==target)return new int[]{i,j};
            }
        }
        return new int[]{-1,-1};
    }
}