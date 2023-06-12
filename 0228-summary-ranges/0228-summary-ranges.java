class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ans=new LinkedList<>();
        int n=nums.length;
        int start=0;
        while (start<n){
            int end=start+1;
            while (end<n && (nums[end] - nums[end-1]==1))end++;
            ans.add((start == end-1)?nums[start]+"" : nums[start]+"->"+nums[end-1]);  
            start=end;
        } 
        return ans;
    }
}