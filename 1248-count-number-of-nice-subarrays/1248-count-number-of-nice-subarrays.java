class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
       int n = nums.length;
        int[] prefix = new int[n + 1];

        //detect odd and even
        for (int i = 0; i < n; i++) {
            nums[i] = (nums[i] % 2)==0?0:1;
        }

        //add prefix
        for (int i = 1; i <=n; i++) {
            prefix[i] = prefix[i-1] + nums[i-1];
        }

        int res=0;
        Map<Integer, Integer> sumPrefixMap = new HashMap<>();
         sumPrefixMap.put(0, 1);
        for (int i = 1; i <= n; i++) {
             sumPrefixMap.merge(prefix[i], 1, Integer::sum);
             if (sumPrefixMap.containsKey(prefix[i] - k)) {
                    res += sumPrefixMap.get(prefix[i] - k);
             }
        }


        return res;
    }
}