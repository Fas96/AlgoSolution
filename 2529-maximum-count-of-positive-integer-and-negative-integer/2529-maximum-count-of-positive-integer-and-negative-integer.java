class Solution {
    public int maximumCount(int[] nums) {
       
      return (int) Math.max(  Arrays.stream(nums).filter(neg->neg<0).count(),Arrays.stream(nums).filter(pos->pos>0).count());

    }
}