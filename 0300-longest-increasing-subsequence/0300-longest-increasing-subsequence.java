class Solution {
    public int lengthOfLIS(int[] nums) {
         TreeSet<Integer> set=new TreeSet<>();
        for (int num : nums) {
            Integer ceiling = set.ceiling(num);
            System.out.print(ceiling);
            if(ceiling!=null)set.remove(ceiling);
            
            set.add(num);
        }
        return set.size();
    }
}