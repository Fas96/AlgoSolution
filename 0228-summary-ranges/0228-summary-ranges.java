class Solution {
    public List<String> summaryRanges(int[] nums) {
         List<String> ans=new LinkedList<>();
        int n=nums.length;
        int i=0;
        while (i<n){
            int j=i+1;
            while (j<n && (nums[j] - nums[j-1]==1)){
                j++;
            }
            if (i == j-1) ans.add(nums[i]+""); 
            else ans.add(nums[i]+"->"+nums[j-1]);
            i=j;
        } 
        return ans;
    }
}