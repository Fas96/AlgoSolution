class Solution {
    public int search(int[] nums, int target) {
         int low=0,high=nums.length-1;
        while (low<=high){
            int pivot=low+(high-low)/2;
            if (nums[pivot]==target)return pivot;
            else if (nums[pivot]<target)low=pivot+1;
            else high=pivot-1;
        }
        return -1;
    }
}