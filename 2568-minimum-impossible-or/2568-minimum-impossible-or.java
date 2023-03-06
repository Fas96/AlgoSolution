class Solution {
    public int minImpossibleOR(int[] nums) {
         Set<Integer> list = new HashSet<>();
       
        for (int nn:nums) list.add(nn);
        
        int p=1;
     
        for(int i=1;list.contains(p) && i<100000;i++){
            p=(int)Math.pow(2,i);
        }
          
        return (int) p;
    }
}