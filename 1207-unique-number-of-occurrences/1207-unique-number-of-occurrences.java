class Solution {
    public boolean uniqueOccurrences(int[] arr) {
          Map<Integer,Integer> freq=new HashMap<>();
        for (int n : arr) {
            freq.merge(n,1,Integer::sum);
        }
       return freq.size()==freq.values().stream().distinct().count(); 

    }
}