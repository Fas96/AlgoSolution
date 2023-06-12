class Solution {
    public List<String> summaryRanges(int[] nums) {
         List<String> ans=new LinkedList<>();
        int n=nums.length;
        int i=0;
        while (i<n){
            int j=i+1;
            while (j<n && (nums[j] - nums[j-1]==1))j++;
            ans.add((i == j-1)?nums[i]+"" : nums[i]+"->"+nums[j-1]);  
            i=j;
        } 
        return ans;
    }
}