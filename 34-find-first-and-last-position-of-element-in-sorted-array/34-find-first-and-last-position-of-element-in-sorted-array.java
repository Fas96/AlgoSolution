class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res= {-1,-1};
   if(nums.length==0 || Arrays.stream(nums).noneMatch(e->e==target)){
     return  res;
   };

   int low=0,high=nums.length-1;
   while (low<high){
     int mid=(low+high)/2;
     int dum = nums[mid] < target ? (low = mid + 1) : (high = mid);
   }
   if(nums[low]!=target){
     return res;
   }
   res[0]=low;

   high=nums.length-1;
   while (low<high){
     int mid=(low+high+1)/2;
     int dum = nums[mid] > target ? (high = mid - 1) : (low = mid);
   }

    res[1]=low;
    System.out.println(Arrays.toString(res));
   return res;
    }
}