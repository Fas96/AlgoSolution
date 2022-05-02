class Solution {
    public int[] sortArrayByParity(int[] nums) {
           int[] events = Arrays.stream(nums).filter(e -> e % 2 == 0).toArray();
        int[] ords = Arrays.stream(nums).filter(e -> e % 2 == 1).toArray();
        int[] resa=new int[nums.length];
        List<Integer> res= new ArrayList<>();
        for (int e : events) {
            res.add(e);
        }
        for (int e : ords) {
            res.add(e);
        }
        for (int i = 0; i < res.size(); i++) {
            resa[i]=res.get(i);
        }

        return resa; 
    }
}