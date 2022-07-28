class Solution {
  public boolean isAnagram(String s, String t) {
    Map<Character, ArrayList<Character>> str1Map= new HashMap<>();
    Map<Character, ArrayList<Character>> str2Map= new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
      str1Map.putIfAbsent(s.charAt(i),new ArrayList<>());
      str1Map.get(s.charAt(i)).add(s.charAt(i));
    }
    for (int i = 0; i < t.length(); i++) {
      str2Map.putIfAbsent(t.charAt(i),new ArrayList<>());
      str2Map.get(t.charAt(i)).add(t.charAt(i));
    }
 
    return areMapsEqual(str1Map,str2Map);
  }
  boolean areMapsEqual(Map<Character, ArrayList<Character>> m1, Map<Character, ArrayList<Character>> m2) {
    if (m1.size() != m2.size()) { return false; }
    return m1.entrySet().stream()
        .allMatch(e -> e.getValue().equals(m2.get(e.getKey())));
  }
}