class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        Arrays.sort(nums);
       
        
       List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        
          int end = 0;
        for(int i = 0; i < nums.length; i++) {
            int e = nums[i];
            int start = i > 0 && nums[i] == nums[i - 1] ? end : 0;
            end = res.size();
            for(int j = start; j < end; j++) {
                List<Integer> sub = new ArrayList<>(res.get(j));
                sub.add(e);
                res.add(sub);
            }
        }
        return res;
        
        
        
    }
}