class Solution {
    public int[] sortedSquares(int[] nums) {
  nums=Arrays.stream(nums).map(e->e*e).toArray();
    Arrays.sort(nums);
    return nums;
    }
}