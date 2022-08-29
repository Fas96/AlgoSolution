class Solution {
  public int removeDuplicates(int[] nums) {
    int L=0,R=1;
    while ( R<nums.length){
    
      if(nums[L]!=nums[R]) {
        L++;
        swap(nums, L, R);
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