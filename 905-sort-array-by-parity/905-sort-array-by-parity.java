class Solution {
    public int[] sortArrayByParity(int[] nums) {
          return Arrays
		.stream(nums)
		.boxed()
		.sorted((a, b) -> Integer.compare(a % 2, b % 2))
		.mapToInt(Integer::intValue)
		.toArray();
    }
}