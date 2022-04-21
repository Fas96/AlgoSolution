class Solution {
    public int mostFrequent(int[] nums, int key) {
           Map<Integer, Integer> counts = new HashMap<>();

        for (int i = 0; i < nums.length - 1; i++) {
            int numsKey = nums[i];
            int numsValue = nums[i + 1];
            if (numsKey == key) {
                counts.put(numsValue, counts.getOrDefault(numsValue, 0) + 1);
            }
        }

        int maxValue = 0;
        int maxCount = 0;
        System.out.println(counts);

        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            int specKey = entry.getKey();
            int specValue = entry.getValue();

            if (specValue > maxCount) {
                maxValue = specKey;
                maxCount = specValue;
            }
        }

        return maxValue;
    }
}