class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> hm= new HashMap<>();
        int[]res=new int[k];

        for (int n : nums) {hm.merge(n,1,Integer::sum);}
        final int[] cnt = {0};
       hm.entrySet().stream().sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed()).forEach(e->{
           if(cnt[0] <k){
           res[cnt[0]++]= (int) e.getKey();}
       });
        return res;
     }
}