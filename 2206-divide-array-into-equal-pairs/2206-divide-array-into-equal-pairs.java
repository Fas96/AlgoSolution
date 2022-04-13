class Solution {
    public boolean divideArray(int[] nums) {
         Map<Integer,Integer> resss= new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            Integer j=resss.getOrDefault(nums[i],-1);
            resss.put(nums[i],(j==-1?1:j+1) );
        }
        for (Map.Entry<Integer, Integer> entry : resss.entrySet()) { 
            if(entry.getValue()%2==1)return false;
        }

        return true;
    }
}