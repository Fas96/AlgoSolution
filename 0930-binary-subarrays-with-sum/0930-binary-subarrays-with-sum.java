class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for (int i = 1; i <=n; i++) {
            prefix[i] = prefix[i-1] + nums[i-1];
        }
        int res=0;
        Map<Integer, Integer> sumPrefixMap = new HashMap<>();
        sumPrefixMap.put(0, 1);
        System.out.println(Arrays.toString(prefix));
        for (int i = 1; i <=n; i++) {
            if (sumPrefixMap.containsKey(prefix[i] - goal)) {
                res += sumPrefixMap.get(prefix[i] - goal);
            }
            sumPrefixMap.merge(prefix[i], 1, Integer::sum);
        }
        return res;
    }
}