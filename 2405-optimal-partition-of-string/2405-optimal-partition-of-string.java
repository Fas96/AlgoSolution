class Solution {
    public int partitionString(String s) {
      int max =(s.isEmpty())? 0:1;
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if(map.containsKey(s.charAt(i))){
                map.clear();
                max++;
            }
            map.put(s.charAt(i), 1);
        }
        return max;
    }
}