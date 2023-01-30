class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
          int n = nums.length;

        Map<Integer, Integer> sumPrefixMap = new HashMap<>();
        sumPrefixMap.put(0, -1);
        int sum = 0;

        for (int i = 0; i <n; i++) {
            sum += nums[i];
            if (k != 0) {
                sum = sum % k;
            }
            if (sumPrefixMap.containsKey(sum)) {
                if(i - sumPrefixMap.get(sum) > 1) {
                    return true;
                }
            }else {
                sumPrefixMap.put(sum, i);
            }

        }
        return false;
    }
}