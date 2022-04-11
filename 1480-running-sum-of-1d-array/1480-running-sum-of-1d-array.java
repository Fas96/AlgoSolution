class Solution {
    public int[] runningSum(int[] nums) {
        
    ArrayList<Integer> a = new ArrayList<>(nums.length);
        for (int n : nums) {a.add(n);}
        int[]  res= new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i]=sumList(new ArrayList<>(a.subList(0, i+1)));
        }
        return res;
    }

    private   int sumList(List<Integer> collect) {
        int t=0;
        for (Integer n : collect) {t+=n;}
        return t;
    }
}