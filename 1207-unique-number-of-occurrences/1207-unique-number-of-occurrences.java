class Solution {
    public boolean uniqueOccurrences(int[] arr) {
          Map<Integer,Integer> freq=new HashMap<>();
        for (int n : arr) {
            freq.merge(n,1,Integer::sum);
        }
        return freq.values().stream().allMatch(v -> freq.values().stream().filter(v1 -> Objects.equals(v1, v)).count() == 1);

    }
}