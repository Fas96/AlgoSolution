class Solution {
    public int[] sortedSquares(int[] nums) {
         return Arrays.stream(Arrays.stream(nums).map(i->i*i).toArray()).sorted().toArray();
    }
}