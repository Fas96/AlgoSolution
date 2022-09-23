class Solution {
    public int arrayNesting(int[] nums) {
          int ans=0;
        Set<Integer> set=new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if(!set.contains(i)){
                int count=0;
                int index=i;
                while(!set.contains(index)){
                    set.add(index);
                    index=nums[index];
                    count++;
                }
                ans=Math.max(ans,count);
            }
        }
        return ans;
    }
}