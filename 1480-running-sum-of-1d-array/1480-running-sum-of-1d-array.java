class Solution {
    public int[] runningSum(int[] nums) {
     
        ArrayList<Integer> a = new ArrayList<>(nums.length);

        for (int n : nums) {a.add(n);}
        int[]  res= new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i]= (int) a.subList(0, i+1).stream().mapToLong(Integer::longValue).sum();;
        }
        return res;
    }
}