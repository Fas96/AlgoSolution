class Solution {
    public int threeSumClosest(int[] arr, int targetSum) {
         if(arr==null||arr.length<3) return -1;

        Arrays.sort(arr);
        int smallestDiff=Integer.MAX_VALUE;
        for (int i = 0; i < arr.length-2; i++) {
            int left=i+1,right=arr.length-1;
            while(left<right){
                int targetDiff=targetSum-arr[i]-arr[left]-arr[right];
                if(targetDiff==0){
                    return targetSum-targetDiff;
                }
                if(Math.abs(targetDiff)<Math.abs(smallestDiff)||(Math.abs(targetDiff)==Math.abs(smallestDiff)&&targetDiff>smallestDiff)){
                    smallestDiff=targetDiff;
                }
                if(targetDiff>0){
                    left++;
                }else{
                    right--;
                }
            }
        }
        return targetSum-smallestDiff;
    }
}