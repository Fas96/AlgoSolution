class Solution {
    public boolean containsDuplicate(int[] nums) {
             HashMap<Integer,Integer>   map=new HashMap<>();
        for (int a : nums) {
             if(map.containsKey(a)) return true;
             map.put(a,1);
        }
        return false;
    }
}