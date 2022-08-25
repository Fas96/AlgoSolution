class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
    Map<Character,Integer> rMap= new HashMap<>();
    Map<Character,Integer> mMap= new HashMap<>();
    for (int i = 0; i < ransomNote.length(); i++) {
      rMap.merge(ransomNote.charAt(i),1,Integer::sum);
    }
    for (int i = 0; i < magazine.length(); i++) {
      mMap.merge(magazine.charAt(i),1,Integer::sum);
    }

  return   rMap.entrySet().stream().allMatch(e->mMap.getOrDefault(e.getKey(),0)>=e.getValue());

    }
}