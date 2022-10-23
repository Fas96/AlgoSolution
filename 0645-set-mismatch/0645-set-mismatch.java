class Solution {
    public int[] findErrorNums(int[] nums) {
         int[] res= new int[2];
        Map<Integer,Integer> mp= new TreeMap<>();
        for (int i = 0; i < nums.length; i++) {
            mp.merge(nums[i],1,Integer::sum);
        }
        for (int i = 1; i <=nums.length; i++) {
            if(mp.get(i)!=null && mp.get(i)==2){
                res[0]=i;
            }
            if(mp.get(i)==null ){
                res[1]=i;
            }

        }
        return res;
    }
}