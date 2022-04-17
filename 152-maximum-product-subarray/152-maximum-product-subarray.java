class Solution {
    public int maxProduct(int[] nums) {
 
          if(nums.length <=1) return nums[0];

        int min[] = new int[nums.length];
        min[0] = nums[0];

        int max[] = new int[nums.length];
        max[0] = nums[0];

        int res = nums[0];

        for(int i = 1; i < nums.length; i++) {
            int minAtIdx= Math.min(max[i - 1] * nums[i], nums[i]);
            int maxAtIdx=Math.max(max[i - 1] * nums[i], nums[i]);
            min[i] = Math.min(min[i - 1] * nums[i],minAtIdx);
            max[i] = Math.max(min[i - 1] * nums[i], maxAtIdx);
            if(max[i] > res) res = max[i];
        }

        return res;
    }
}