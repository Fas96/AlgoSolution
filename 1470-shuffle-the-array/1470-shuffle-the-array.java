class Solution {
    public int[] shuffle(int[] nums, int n) {
          List<Integer> ansList = new ArrayList<>();
        for (int i = 0; i < n; i++) { 
            ansList.add(nums[i]);
            ansList.add(nums[i+n]);
        }
        return ansList.stream().mapToInt(i->i).toArray();
    }
}