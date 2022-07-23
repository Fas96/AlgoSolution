class Solution {
  /*  public List<Integer> countSmaller(int[] nums) {
         List<Integer> res=new ArrayList<>();
    for (int i = 0; i < nums.length; i++) {
      int c=0;
      for (int j = i; j < nums.length; j++) {
        if(nums[i]>nums[j])c++;
      }
      res.add(c);
    }
    System.out.println(res);

    return  res;
    }
    */
    
    public List<Integer> countSmaller(int[] nums){
    List<Integer> res = new LinkedList<Integer>();
    if (nums == null || nums.length == 0) {
      return res;
    }
    // find min value and minus min by each elements, plus 1 to avoid 0 element
    int min = Integer.MAX_VALUE;
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < nums.length; i++) {
      min = (nums[i] < min) ? nums[i]:min;
    }
    int[] nums2 = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
      nums2[i] = nums[i] - min + 1;
      max = Math.max(nums2[i],max);
    }
    int[] fenwickTree = new int[max+1];
    for (int i = nums2.length-1; i >= 0; i--) {
      res.add(0,getFenwickTree(nums2[i]-1,fenwickTree));
      updateFenwickTree(nums2[i],fenwickTree);
    }
    return res;
  }

  private int getFenwickTree(int i, int[] fwtree) {
    int num = 0;
    while (i > 0) {
      num +=fwtree[i];
      i -= i&(-i);
    }
    return num;
  }
  private void updateFenwickTree(int i, int[] fwtree) {
    while (i < fwtree.length) {
      fwtree[i] ++;
      i += i & (-i);
    }
  }
}