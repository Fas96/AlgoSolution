class Solution {
    public int minOperations(int[] nums) {
        HashMap<Integer,Integer> fmap = new HashMap<>();
       int operations=0;
       for(int val : nums){
           fmap.put(val,fmap.getOrDefault(val,0)+1);
       }
       for(int key : fmap.keySet()){
           if(fmap.get(key)==1){
               return -1;
           }
           else if(fmap.get(key)%3==0){
               operations += (fmap.get(key)/3);
           }else{
               operations += (fmap.get(key)/3) + 1;
           }  
       }
        return operations;
    }
}