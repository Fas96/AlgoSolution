class Solution {
    public int findUnsortedSubarray(int[] nums) {
         int low=0,high=nums.length-1;
         
        while (low<nums.length-1&&nums[low]<=nums[low+1]){
            low++;
        }
        if(low==nums.length-1){
            return 0;
        }
         
        while (high>0&&nums[high]>=nums[high-1]){
            high--;
        }
         
        int min=Integer.MAX_VALUE,max=Integer.MIN_VALUE;
        for (int i = low; i <=high; i++) {
            min=Math.min(min,nums[i]);
            max=Math.max(max,nums[i]);
        }
        
        
        while (low>0&&nums[low-1]>min){
            low--;
        }
       
        while (high<nums.length-1&&nums[high+1]<max){
            high++;
        }
        return high-low+1;
    }
}