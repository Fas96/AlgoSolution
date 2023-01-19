class Solution {
    public int subarraysDivByK(int[] nums, int k) {
       int totalCount = 0, sum = 0,n=nums.length;
        Map<Integer,Integer> map = new HashMap<>();
        map.put(0,1);
        for(int i=0;i<n;i++){
            sum += nums[i];

            int mod = sum % k;

           if(mod < 0)mod += k;

            if(map.containsKey(mod)){
                totalCount += map.get(mod);
                map.merge(mod, 1, Integer::sum);
            } else {
                map.put(mod, 1);
            }
        }
        return totalCount;
    }
}