class Solution {
    public int singleNonDuplicate(int[] nums) {  HashMap<Integer, Integer> map = new HashMap<>();
        for (int num :nums)map.merge(num, 1, Integer::sum);
        
        return map.entrySet().stream().filter(e->e.getValue()==1).findFirst().get().getKey();

        
    }
}