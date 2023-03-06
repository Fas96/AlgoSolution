class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        if(minK>maxK)return 0;
        int n = nums.length;
        long res = 0;
        int mn=-1,mx=-1,l=-1;
        for(int i=0;i<n;i++){
           if(nums[i]<minK||nums[i]>maxK)l=i;
           if(nums[i]==minK)mn=i;
           if(nums[i]==maxK)mx=i;
           int r = Math.min(mn,mx);
           if(r>l)res+=r-l;
        }
        return res;
    }

    
}