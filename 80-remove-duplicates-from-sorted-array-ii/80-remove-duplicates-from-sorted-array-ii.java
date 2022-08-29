class Solution {
    public int removeDuplicates(int[] nums) {
        
    int L=0,R=1,C=0;
    while ( R<nums.length){
    
      if(nums[L]!=nums[R]) {
        L+=1;
        swap(nums, L, R);
        C=0; 
      }else if(nums[L]==nums[R] && C<1){
          C++;
          L++;
          nums[L]=nums[R];
      }
   
      R++;
      
      
    }
    return L+1;
  }
  private void swap (int[] a, int i, int j) {
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
  }
}