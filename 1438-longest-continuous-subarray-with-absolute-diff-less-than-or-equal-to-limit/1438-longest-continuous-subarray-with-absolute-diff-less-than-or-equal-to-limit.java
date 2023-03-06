class Solution {
    public int longestSubarray(int[] nums, int limit) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        int l = 0, r = 0, res = 0;
        while (r < nums.length) {
            map.put(nums[r], map.getOrDefault(nums[r], 0) + 1);
            while (map.lastKey() - map.firstKey() > limit) {
                map.put(nums[l], map.get(nums[l]) - 1);
                if (map.get(nums[l]) == 0) map.remove(nums[l]);
                l++;
            }
            res = Math.max(res, r - l + 1);
            r++;
        }
        return res;
    }
}