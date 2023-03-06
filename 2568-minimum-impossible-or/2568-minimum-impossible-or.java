class Solution {
    public int minImpossibleOR(int[] nums) {
           int y=0;
          for (int nb :nums){
            if((nb & (nb-1))==0){y|=nb;}
        }
        for(int i=0;i<30;i++){
            if((y>>i & 1)==0)return 1<<i;
        }
        
        return 1<<30;
        
    }
}
/*    
        001
        010
        011
        100
        101
        110
        111
        

        int n = nums.length;
        int nonExperssable = -1;
        Set<Integer> list = new HashSet<>();
        for (int nb :nums)list.add(nb);
        for (int i = 0; i < n-1; i++) {
            list.add(nums[i]| nums[i+1]);
        }

        Collections.sort(new ArrayList<>(list));
        
        for (int i = 1; i < 100000; i++) { 
            if(!list.contains(i))return i;
        }

        return nonExperssable;
*/
//[1,25,2,72]
//2,3,4,
//2,