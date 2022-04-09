class Solution {
    public int[] topKFrequent(int[] nums, int k) {
         ArrayList<Integer> nNums= new ArrayList<>(nums.length);

        for (int n : nums) {
            nNums.add(n);
        }
        // hashmap to store the frequency of element
        Map<Integer, Integer> hm = new HashMap<Integer, Integer>();

        for (Integer i : nNums) {
            Integer j = hm.get(i);
            hm.put(i, (j == null) ? 1 : j + 1);
        } 

        LinkedHashMap<Integer, Integer> sortedMap = new LinkedHashMap<>();

        hm.entrySet().stream().sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())).forEachOrdered(x -> sortedMap.put(x.getKey(), x.getValue()));
        int[] res= new int[k];
        int i=0;
        for (Map.Entry<Integer, Integer> val : sortedMap.entrySet()) {
            if(i<k){  res[i]=val.getKey();i++;}
        }
        return res;
    }
}