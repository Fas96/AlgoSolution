class Solution {
    public String frequencySort(String s) {
       HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        int[] index = new int[256];
        for (int i = 0; i < 256; i++) {
            index[i] = i;
        }
        for (int i = 0; i < 256; i++) {
            for (int j = i + 1; j < 256; j++) {
                if (map.getOrDefault((char) index[i], 0) < map.getOrDefault((char) index[j], 0)) {
                    int temp = index[i];
                    index[i] = index[j];
                    index[j] = temp;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 256; i++) {
            if (map.getOrDefault((char) index[i], 0) == 0) {
                break;
            }
            for (int j = 0; j < map.get((char) index[i]); j++) {
                sb.append((char) index[i]);
            }
        }
        return sb.toString();
    }
}