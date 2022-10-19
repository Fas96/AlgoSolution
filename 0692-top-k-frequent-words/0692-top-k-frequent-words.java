class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        List<String> result = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for(String word : words){
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        
        List<String> candidates = new ArrayList<>(map.keySet());
        candidates.sort((w1, w2) -> map.get(w1).equals(map.get(w2)) ? w1.compareTo(w2) : map.get(w2) - map.get(w1));
        
        for(int i = 0; i < k; i++){
            result.add(candidates.get(i));
        }
        
        return result;
    }
}