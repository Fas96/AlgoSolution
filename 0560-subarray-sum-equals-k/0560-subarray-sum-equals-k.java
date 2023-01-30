class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for (int i = 1; i <=n; i++) {
            prefix[i] = prefix[i-1] + nums[i-1];
        }
        int res=0;
        Map<Integer, Integer> sumPrefixMap = new HashMap<>();
        sumPrefixMap.put(0, 1);
        for (int i = 1; i <=n; i++) {
            if (sumPrefixMap.containsKey(prefix[i] - k)) {
                res += sumPrefixMap.get(prefix[i] - k);
            }
            sumPrefixMap.merge(prefix[i], 1, Integer::sum);
        }
        return res;
    }
}