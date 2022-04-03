class Solution {
    public int[] twoSum(int[] nums, int target) {
            int [] index= new int[2];

            for (int i = 0; i < nums.length; i++) {
                for (int j = 0; j < nums.length; j++) {
                    if((nums[i]+nums[j])==target && i !=j){
                        index[0]=i;
                        index[1]=j;
                        return index;
                    }
                }
            }


            return index;  
    }
}