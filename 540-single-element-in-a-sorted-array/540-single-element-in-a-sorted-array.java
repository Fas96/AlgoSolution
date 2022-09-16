class Solution {
    public int singleNonDuplicate(int[] nums) {
     int L=0,mid=0, H=nums.length-1;
        while(L<H){
            mid = (L + H) /2;
                if (nums[mid] == nums[mid ^ 1])
                    L = mid + 1;
                else
                    H = mid;
     }
        return nums[L];
    }
}