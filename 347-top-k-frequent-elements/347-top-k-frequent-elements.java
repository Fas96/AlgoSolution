import java.util.concurrent.atomic.AtomicInteger;
class Solution {
  public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> hm= new HashMap<>();
        int[]res=new int[k];

        for (int n : nums) {hm.merge(n,1,Integer::sum);}
         AtomicInteger cnt = new AtomicInteger();
       hm.entrySet().stream().sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed()).forEach(e->{
           if(cnt.get() <k){
           res[cnt.getAndIncrement()]= (int) e.getKey();
           }
       });


        return res;
     }
}