class Solution {
    public int search(int[] nums, int target) {
        int L=0,mid=0,H=nums.length-1;
         
        while(L<=H){
            mid=(L+H)/2;
            if(nums[mid]==target)return mid;
            if(target>nums[mid])L=mid+1;
            if(target<nums[mid])H=mid-1;
        }
        
        return -1;
    }
}